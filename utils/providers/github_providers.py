import aiohttp
import asyncio

class GitHub:
    def __init__(self, token: str):
        self.session = aiohttp.ClientSession()
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    async def get_user(self, username: str):
        async with self.session.get(f"https://api.github.com/users/{username}", headers=self.headers) as response:
            return await response.json()

    async def get_repos(self, username: str):
        async with self.session.get(f"https://api.github.com/users/{username}/repos", headers=self.headers) as response:
            return await response.json()

    async def get_users_projects(self, user: str):
        query = """{user(login: \"USER\") {projectsV2(first: 20) {nodes {id title}}}}"""

        query = query.replace("USER", user)
        async with self.session.post("https://api.github.com/graphql", headers=self.headers,
                                     json={"query": query}) as response:
            data = await response.json()
            return data['data']['user']['projectsV2']['nodes']

    async def get_organization_projects(self, organization: str):
        query = """{organization(login: \"ORGANIZATION\") {projectsV2(first: 20) {nodes {id title}}}}"""

        query = query.replace("ORGANIZATION", organization)
        async with self.session.post("https://api.github.com/graphql", headers=self.headers,
                                     json={"query": query}) as response:
            data = await response.json()
            return data['data']['organization']['projectsV2']['nodes']

    async def get_project(self, project_id: str):
        query = """ 
            query{ node(id: \"PROJECT_ID\") { ... on ProjectV2 { items(first: 20) { nodes{ id fieldValues(first: 8) { nodes{ ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon {  name }}} ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } } ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name }}}}} content{ ... on DraftIssue { title body } ...on Issue { title assignees(first: 10) { nodes{ login }}} ...on PullRequest { title assignees(first: 10) { nodes{ login }}}}}}}}}
        """

        query = query.replace("PROJECT_ID", project_id)
        async with self.session.post("https://api.github.com/graphql", headers=self.headers,
                                     json={"query": query}) as response:
            data = await response.json()
            return data['data']['node']['items']['nodes']


    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


async def main():
    async with GitHub("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") as client:
        # user = await client.get_user("carlosjeff")
        # repos = await client.get_organization_projects("s1mbi0se")
        project = await client.get_project('PVT_kwDOADeI584AJSxc')

        # print(user)
        print(project)


if __name__ == '__main__':
    asyncio.run(main())