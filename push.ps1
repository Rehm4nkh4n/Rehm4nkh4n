$git = "C:\Program Files\Git\bin\git.exe"
$repo = "c:\Users\ASUS\Downloads\github-profile-readme-upload\github_readme_build"

& $git -C $repo config user.name "Rehm4nkh4n"
& $git -C $repo config user.email "Rehm4nkh4n@users.noreply.github.com"
& $git -C $repo add .
& $git -C $repo commit -m "first commit"
& $git -C $repo branch -M main
& $git -C $repo push -u origin main
