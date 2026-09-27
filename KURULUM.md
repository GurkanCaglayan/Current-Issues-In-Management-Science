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

# Orca ayarları

Orca'da ayar aktarma yok, Settings ekranından elle girilir.

Önce fontlar:
- Cascadia Mono: yoksa `winget install Microsoft.CascadiaCode`
- Geist: github.com/vercel/geist-font

| Ayar | Değer |
|---|---|
| Theme | System |
| App font | Geist |
| Terminal font | Cascadia Mono Light |
| Terminal font size | 13 |
| Terminal font weight | 500 |
| Terminal line height | 1 |
| Terminal theme (dark) | Gruvbox Dark |
| Ayrı açık tema | Açık |
| Terminal theme (light) | Builtin Tango Light |
| Cursor style | Bar |
| Windows shell | powershell.exe |
| UI language | System |
| Editor font | boş |
