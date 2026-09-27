# MAN403 dersi ve Fossoglor projesi

Üst klasördeki `CLAUDE.md` burada da geçerlidir: projeyi ben yürütürüm, Claude kontrol eder ve gerektiğinde öğretir.

## Amaç

MAN403 Selected Topics in Management Science (Hacettepe, Dr. Mustafa Çimen, Güz 2026) dersinin
haftalık takibi ve P2 Fossoglor projesinin kodu ve raporları.

## Klasörler

| Klasör | Amacı |
|---|---|
| `docs/` | Ders belgeleri: `syllabus.pdf`, `project-booklet.pdf`. Değiştirilmez. |
| `haftaNN/` | O haftanın konusu ve ödevleri. |
| `hafta06-project1/`, `hafta10-project2/`, `hafta14-project3/` | Proje teslim haftaları ve raporları. |
| `fossoglor/` | Fossoglor simülatörü ve yöntemlerin Python kodu. |

## Takvim

| Proje | Yöntem | Teslim | Not |
|---|---|---|---|
| 1 | Gurobi ile LP/MIP tabanlı sezgisel | Hafta 6, 27.10.2026 | %15 |
| 2 | Kısıtlı veya simülasyon tabanlı dinamik programlama | Hafta 10, 24.11.2026 | %15 |
| 3 | Temporal-difference (TD) öğrenme | Hafta 14, 22.12.2026 | %15 |
| Final | Karşılaştırmalı rapor ve sözlü sınav | Bölüm duyuracak | %50 |

## Fossoglor (kitapçıktan)

- 8 ürün, 1 üretim hattı, sınırlı haftalık çalışma saati, her ürün için hazırlık (setup) süresi ve maliyeti.
- Belirsiz olan: her ürünün haftalık talebi.
- Karşılanamayan sipariş bekler, beklediği her hafta için ceza ödenir.
- Planlama ufku: 12 hafta.
- Amaç: hazırlık, stok ve geciken sipariş maliyetlerinin toplamını en aza indirmek.
- Basit başlangıç kuralı: "Her pazartesi, stoku bir haftadan az kalan ürünlere bak. Stoku en az olandan başlayarak, hattın saatleri yettiği sürece üç haftalık üretim yap."
- Okuma: Tempelmeier (2013), Stochastic lot sizing problems.

## Claude neyi kontrol eder

Kodumu ve raporumu okurken Claude şu kurallara uyulup uyulmadığını kontrol eder:

1. Önce basit kural kodlanmış mı? Her yöntem ona göre ölçülür.
2. Simülatör 100 kez, her çalışmadan önce `random.seed(k)` (k = 1, ..., 100) ile çalışıyor mu? Tüm yöntemler aynı seed'leri mi kullanıyor?
3. Deneme ve ayarda 1000 ve üstü seed'ler mi kullanılmış?
4. Sonuç tablosunda ortalama maliyet, en yüksek maliyet, basit kurala göre iyileşme (%) ve hesaplama süresi var mı?
5. Seçilen her sayının nereden geldiği raporda yazıyor mu?
6. Kullanılan her kaynak belirtilmiş mi?
7. Kod, hoca derste değişiklik istediğinde (kısıt ekleme, maliyet değiştirme) benim değiştirebileceğim kadar açık mı?

## Gurobi

Gurobi'yi Excel Solver bilgimden yola çıkarak öğreniyorum. Claude önce Solver'daki karşılığını gösterir
(değişken hücreler = karar değişkenleri, kısıt listesi = kısıtlar), `gurobipy` yazımını ben denerim, Claude kontrol eder.
