<!-- cd C:/Users/jsteenkamp/Projects/testim
python -m venv venv
.\venv\Scripts\activate
py -m pip install --upgrade pip
pip install -r requirements.txt -->
cd C:/Users/jsteenkamp/Projects/testim
git init
git add .
git commit -m "Initial commit"

<!-- Create a new repository on GitHub: Go to GitHub and create a new repository. Do not initialize it with a README, .gitignore, or license, as you already have a local repository.

Add the remote repository: Add the remote repository URL to your local Git repository. Replace YOUR_GITHUB_USERNAME and YOUR_REPOSITORY_NAME with your GitHub username and the name of the repository you created: -->

git remote add origin https://github.com/jacquesonline/jiraendpoint.git
git push -u origin master

curl --request GET \
--url 'https://yoursitename.atlassian.net/rest/api/3/filter/search?filterName=YourFilterName' \
--user 'youremail@mail.com:yourapitoken' \
--header 'Accept: application/json'
