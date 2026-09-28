# Fossoglor şirket hikâyesi

Bu dosya, `problem.md` B bölümündeki sayıların arkasındaki hikâyeyi toplar. Sayıların kendisi `problem.md` dosyasında; burada yalnızca "neden bu sayı" var. Rapora dönüştürülecek.

## Şirket ve üretim hattı

- Fossoglor, otomotiv yan sanayinde metal parça (dişli, mil, valf gövdesi vb.) üreten bir şirkettir.
- Üretim tek bir CNC hattında yapılır (kitapçık: 1 üretim hattı).
- **Haftalık çalışma saati (120 saat):** hat 3 vardiyayla haftanın 5 günü kesintisiz çalışır (5 × 24).
- **Setup süresi (2 saat):** bir üründen diğerine geçerken CNC'de takım ve bağlama aparatı değişimi.
- **Birim üretim süresi (15 dk):** parçanın işlenmesi ve kalite kontrolü.
- **Setup maliyeti tüm ürünlerde aynı (300 $):** maliyeti ürün değil, makinenin doğası belirler.

## Stok maliyeti

- Stok maliyeti, stoktaki her ek adetle artan maliyettir: parçaya bağlanan sermaye, pas önleyici bakım, sigorta.
- Deponun sabit giderleri (kira, sabit personel) stok miktarından bağımsız olduğu için stok maliyetine dahil değildir.
- Parçaların boyutu ve değeri birbirine yakındır; fark, ürün grubunun sözleşme şartlarından gelir (aşağıda).

## Ürün grupları

### Ürün 1–2: sözleşmeli ürünler

- **Ürün 1:** fason üretim. Müşterinin talep taahhüdü var → talep çok düzenli (CV 0.1).
- **Ürün 2:** ihale ürünü → talep ürün 1'e göre daha oynak (CV 0.3).
- **Stok maliyeti yüksek (6 $):** sözleşmedeki kalite standartları nedeniyle sigorta ve bakım önemli.
- **Gecikme cezası yüksek (60 $, 50 $):** niş ürünler; müşteri sözleşmeyle bağlı ve gecikmeden doğrudan etkileniyor.

### Ürün 3–5: toptan satış ürünleri

- Toptancılara satılır.
- Talep orta düzeyde oynak (CV 0.2–0.3).
- Stok maliyeti 3 $, gecikme cezası 35 $.

### Ürün 6–8: yedek parçacılara satış

- Birden fazla yedek parçacıya (perakendeciye) tedarik yapılır; aralarında sözleşme yoktur. Perakendeci ürünü hangi tedarikçide bulursa ondan alabilir.
- **Talep oynak (CV 0.45):** rakip tedarikçiler rekabetçi fiyat veriyor; bize gelen sipariş haftadan haftaya değişiyor.
- **Sipariş bekler (kitapçık: backorder):** perakendeci verdiği siparişi iptal etmez; beklediği her hafta bize olan güveni azalır.
- **Gecikme cezası düşük (20 $):** ceza bir ödeme değil, fırsat maliyetidir (kaybedilen gelecek satışlar). Rakipler rekabetçi fiyat verdiği için bu parçaların kâr marjı düşüktür. Fırsat maliyeti kaybedilen marja bağlıdır; marj düşükse müşteriyi kaybetmenin bedeli de düşüktür.
- **Stok maliyeti düşük (2 $):** sözleşmeden gelen ek sigorta ve bakım şartı yoktur.

## Simülasyon modeli

Kod `fossoglor/` klasöründe:

| Dosya | İçinde ne var |
|---|---|
| `parameters.py` | Bütün sayılar (talep, CV, süreler, maliyetler, başlangıç stoku, 120 saat, 12 hafta) |
| `basic_rule.py` | Basit başlangıç kuralı (`simple_rule`): stoğa bakıp bu haftanın üretimini verir |
| `simulator.py` | Talep çekme (`draw_demand`), 12 haftalık bir run, 100 run |

### Bir haftanın akışı

Her hafta, 12 hafta boyunca:

1. **Pazartesi, karar:** `simple_rule` haftanın başındaki stoğa bakar ve 8 ürünün üretim miktarını verir.
2. **Üretim:** üretilen adet stoğa eklenir. Bu hafta üretilen parça bu hafta satılabilir (Tempelmeier 2013, CLSP varsayımı).
3. **Talep:** her ürün için talep çekilir ve stoktan düşülür.
4. **Backlog:** stok eksiye düşerse eksi kısım bekleyen siparişlerdir. Siparişler iptal edilmez, bir sonraki haftaya taşınır ve ilk üretimle kapanır.
5. **Hafta sonu maliyeti:**
   - **Setup:** bir ürün bu hafta üretildiyse (üretim > 0) o ürünün setup maliyeti. Üretim 0 ise setup da yok.
   - **Stok maliyeti:** hafta sonu stoğu > 0 ise stok × o ürünün stok maliyeti. Üretilen adete değil, hafta sonunda depoda kalan adede uygulanır.
   - **Gecikme cezası:** hafta sonu stoğu < 0 ise bekleyen sipariş sayısı × ceza. Sipariş kapanana kadar her hafta yeniden ceza ödenir ("penalty for every week it waits").

12 haftanın maliyetlerinin toplamı = 1 run.

### Basit kuralın ayrıntıları

- Aday ürün: stok < ortalama haftalık talep.
- Sıra: en az stoklu önce.
- Üretim miktarı: 3 × ortalama haftalık talep − stok. Stok eksiyse bekleyen siparişler de bu miktara girer.
- Saat tam üretime yetmezse **kısmi üretim:** setup yapılır, kalan saatle üretilebilecek kadar üretilir, adet aşağı yuvarlanır. Sonra o haftanın üretimi biter.
- Kalan saat setup + 1 adete bile yetmiyorsa o hafta üretim durur, sonraki adaylara bakılmaz. Şu an bütün ürünlerin setup süresi aynı olduğu için bunun bir etkisi yok. Setup süreleri farklılaşırsa, setup'ı daha kısa olan bir sonraki ürün sığabileceği halde atlanmış olur.

### Talep

- Normal dağılım: ortalama = ortalama haftalık talep, standart sapma = CV × ortalama.
- **Neden normal dağılım (kitapçık 1.2):**
  - Normal dağılımda ortalama ve standart sapma ayrı ayrı seçilebilir; böylece her ürünün CV'si ürün grubunun hikâyesine göre belirlenebildi (fason 0.1, yedek parçacı 0.45).
  - Poisson dağılımında varyans = ortalama, yani CV = 1/√ortalama. CV'yi talep belirler, biz seçemeyiz: ürün 1 (ort. 10) için CV ≈ 0.32, ürün 8 (ort. 80) için CV ≈ 0.11 olurdu. Bu, hikâyenin tersidir: en düzenli ürün (fason) en oynak, en oynak ürün (yedek parça) en düzenli olurdu.
  - Kitapçık sade Python istiyor. Normal dağılım Python'un `random` modülünde hazır (`random.gauss`); Poisson için ek kod veya kütüphane (ör. `numpy`) gerekir.
- En yakın tam sayıya yuvarlanır, negatif çıkarsa 0 alınır.
- Çekilişlerin yaklaşık %0.5'i negatif çıkıp 0'a çevriliyor, bu yüzden gerçekleşen ortalama talep çok az yukarı kayıyor (seed 5000, 160 000 çekiliş ile ölçüldü).

### Deney

- Raporlanan sonuçlar: 100 run, her run'dan önce `random.seed(k)`, k = 1, ..., 100 (kitapçık 1.3).
- Deneme ve ayar için seed 1000 ve üstü.
- Hesaplama süresi: 100 run'ın toplam süresi, `time.time()` ile ölçülür.

## Açık konular

- [ ] Ürün 3–5 için hikâye kısa: talep ve maliyetlerin neden orta düzeyde olduğu yazılabilir.
- [x] Neden normal dağılım (kitapçık 1.2) → "Talep" bölümü.
- [ ] Başlangıç stoklarının gerekçesi.
- [ ] Ortalama haftalık taleplerin (10, 20, ..., 80) gerekçesi.
- [ ] Her sayı için kaynak (web araması, ders kitabı, sağduyu), kitapçık 1.1.
