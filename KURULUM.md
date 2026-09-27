# İkinci makinede kurulum

1. Git ve GitHub CLI'yi kur:
   ```
   winget install Git.Git GitHub.cli
   ```
2. GitHub'a giriş yap:
   ```
   gh auth login
   ```
3. Repoyu OneDrive dışındaki bir klasöre indir:
   ```
   cd C:\Users\<kullanıcı>\Projeler
   gh repo clone GurkanCaglayan/Current-Issues-In-Management-Science
   ```
4. Commit'lerde aynı kimlik görünsün diye repo klasöründe:
   ```
   git config user.name "GurkanCaglayan"
   git config user.email "259373090+GurkanCaglayan@users.noreply.github.com"
   ```
