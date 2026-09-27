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

## Açık konular

- [ ] Ürün 3–5 için hikâye kısa: talep ve maliyetlerin neden orta düzeyde olduğu yazılabilir.
- [ ] Her sayı için kaynak (web araması, ders kitabı, sağduyu), kitapçık 1.1.
