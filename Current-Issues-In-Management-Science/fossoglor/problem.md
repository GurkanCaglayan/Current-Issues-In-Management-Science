# Fossoglor (P2)

Bu dosya iki bölümden oluşur:

- **A. Hocanın direktifleri:** kitapçıktan birebir alınmış metin. Değiştirilmez.
- **B. Bizim kararlarımız:** şirket modeli için seçtiğimiz sayılar ve yorumlar. Denedikçe değişir.

---

# A. Hocanın direktifleri

Kaynak: `docs/project-booklet.pdf`, MAN403 Project Booklet, Fall 2026.

## A.1 P2. Fossoglor: what to produce this week

Fossoglor Industries makes 8 products on one production line. Before the line can make a product,
it must be set up for it: a setup takes some hours and costs money. The line has a limited number of
working hours per week. How much of each product customers will order next week is not known in
advance.

Every Monday the production planner decides which products to set up this week and how many
units of each to make. Making large batches saves setups but fills the warehouse; making small batches
keeps stock low but wastes hours on setups. If a customer order cannot be delivered from stock, it
waits until the product is made, and Fossoglor pays a penalty for every week it waits. The planner
plans 12 weeks ahead.

**You choose:** each product's average weekly demand, production time per unit, setup time and setup
cost, the weekly working hours of the line, the cost of keeping a unit in stock for a week, and the
penalty for a late order.

**Uncertain:** each product's weekly demand.

**Goal:** the lowest total cost of setups, stock and late orders over the 12 weeks.

**Simple starting rule:** "Every Monday, look at the products with less than one week of stock.
Starting with the one that has the least stock, produce enough for three weeks, as long as the line's
hours allow."

## A.2 Genel kurallar (bölüm 1.2, 1.3, 1.4, 1.6, 1.7)

### 1.2 Describing what is uncertain

Each story says what the company does not know in advance. The simplest way to describe an
uncertain quantity is a small table of possible values and their chances:


| Daily sales at a store | quiet day | normal day | busy day |
| ---------------------- | --------- | ---------- | -------- |
| units sold             | 8         | 12         | 18       |
| probability            | 0.25      | 0.50       | 0.25     |


In Python, one day's sales can then be drawn with one line:

```python
sales = random.choices([8, 12, 18], weights=[0.25, 0.50, 0.25])[0]
```

If you prefer, you may use a known probability distribution instead (for example the Poisson distribution
for the number of customers). Either way, explain your choice in the report.

### 1.3 Testing your method fairly

- Build a small simulator: a Python function that plays your company's problem day by day (or
week by week), uses your decision rule, draws the uncertain values, and adds up the costs.
- Run the simulator 100 times and take the average. One run plays your company's whole
problem once, with its own draw of the uncertain values.
- Use the same 100 runs for every method you build: before run k (k = 1, ..., 100), write
`random.seed(k)`. Then all your methods face exactly the same "bad days" and "good days", and
the comparison between them is fair.
- While you are still trying things out or tuning a method, use other seeds (for example 1000 and
above), not the seeds you report with.

### 1.4 About the reading lists

Each story ends with a short reading list. These are surveys and problem descriptions: they
explain where the problem comes from, why it is hard, and what people have tried. Read them for
understanding, and cite everything you use.

### 1.6 Start with the simple rule

Every story ends with a simple starting rule: the kind of rule a company might use today without
any analysis. Program it first. It shows that your simulator works, and every method you build is
judged by how much it improves on this rule.

### 1.7 What you submit for each project

1. Your Python code. Plain Python is enough: lists, dictionaries, for loops and if statements.
Clear code matters more than clever code. Project 1 also uses Gurobi, as in MAN305.
2. A short report in the style of an academic paper: the company and your numbers, your method
explained in words, your results, what you learned, and references.
3. The results table below. Use the same table in all three projects.

Comparing with your classmates. Everyone has a different company and everyone chooses their
own numbers, so the costs in your tables cannot be compared with each other: 240 in one project and
1 800 in another mean nothing side by side. What is comparable is the last two columns -- how much
a method improved on its own simple rule, and what it cost in computing time. Those two
numbers, collected across the class, are what the final report discusses.


| Method               | Average cost over the 100 runs | Highest cost among the 100 runs | Improvement over the simple rule (%) | Computing time |
| -------------------- | ------------------------------ | ------------------------------- | ------------------------------------ | -------------- |
| Simple starting rule |                                |                                 | 0                                    |                |
| Your method          |                                |                                 |                                      |                |


---

# B. Bizim kararlarımız (şirket modeli)

Amaç: setup'ın gerçekten karar gerektirdiği, ne çok basit ne çok zor bir problem bulana kadar deneyerek değiştirmek.

## B.1 Parametreler

Para birimi: $.

| Ürün | Ort. haftalık talep (adet) | Birim üretim süresi | Setup süresi | Setup maliyeti | Stok maliyeti ($/adet/hafta) | Gecikme cezası ($/adet/hafta) | Başlangıç stoku (adet) | EOQ (adet) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | 10 | 15 dk | 2 saat | 300 $ | 6 | 60 | 14 | 32 |
| 2 | 20 | 15 dk | 2 saat | 300 $ | 6 | 50 | 18 | 45 |
| 3 | 30 | 15 dk | 2 saat | 300 $ | 3 | 35 | 38 | 77 |
| 4 | 40 | 15 dk | 2 saat | 300 $ | 3 | 35 | 26 | 89 |
| 5 | 50 | 15 dk | 2 saat | 300 $ | 3 | 35 | 64 | 100 |
| 6 | 60 | 15 dk | 2 saat | 300 $ | 2 | 20 | 61 | 134 |
| 7 | 70 | 15 dk | 2 saat | 300 $ | 2 | 20 | 30 | 145 |
| 8 | 80 | 15 dk | 2 saat | 300 $ | 2 | 20 | 24 | 155 |

EOQ = √(2 × D × S / h); D = ort. haftalık talep, S = setup maliyeti, h = ürünün stok maliyeti. En yakın tam sayıya yuvarlandı. Kapasiteyi, setup süresini ve talep belirsizliğini dikkate almaz; sadece referans.

| Parametre | Değer |
| ---- | ---- |
| Hattın haftalık çalışma saati | 120 saat (5 gün × 24 saat) |

Gerekçeler:

- Setup maliyeti tüm ürünlerde aynı: maliyeti ürün değil, makinenin doğası belirliyor.
- Stok maliyeti ve gecikme cezası ürün grubuna göre değişiyor: bkz. `fossoglor company.md`.

## B.2 Talep belirsizliği

- Dağılım: **normal dağılım** (`random.gauss`), ortalama = B.1'deki ort. haftalık talep, standart sapma = CV × ortalama.
- Çekilen talep **en yakın tam sayıya yuvarlanır** (ör. 43.2 → 43, 43.7 → 44).
- Talep **0'dan küçük olamaz**: negatif çıkarsa 0 alınır.

| Ürün | Ort. talep | CV | Standart sapma | Sınıf (XYZ) | Ürün grubu |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | 10 | 0.1 | 1 | X | Sözleşmeli (fason) |
| 2 | 20 | 0.3 | 6 | Y | Sözleşmeli (ihale) |
| 3 | 30 | 0.2 | 6 | X | Toptan |
| 4 | 40 | 0.25 | 10 | X | Toptan |
| 5 | 50 | 0.3 | 15 | Y | Toptan |
| 6 | 60 | 0.45 | 27 | Y | Yedek parçacı |
| 7 | 70 | 0.45 | 31.5 | Y | Yedek parçacı |
| 8 | 80 | 0.45 | 36 | Y | Yedek parçacı |

XYZ eşikleri: X ≤ 0.25, Y 0.25–0.50, Z > 0.50.

Sayıların hikâyesi ve gerekçeleri: `fossoglor company.md`.

## B.3 Basit kuralın yorumu

Kitapçıktaki kural bu noktaları açık bırakıyor; kararlarımız:


| Soru                               | Karar                                                  |
| ---------------------------------- | ------------------------------------------------------ |
| "less than one week of stock"      | `stok < ort. haftalık talep` (eşitlikte üretilmez)     |
| "the one that has the least stock" | Stok **adet** olarak karşılaştırılır                   |
| "produce enough for three weeks"   | Üretim miktarı = 3 × ort. haftalık talep − mevcut stok |
| Saat yetmezse ne olur? | **Kısmi üretim:** setup yapılır, kalan saat kadar üretilir; adet **aşağı yuvarlanır** (ör. (26 − 2) / 0.25 = 96). Kalan saat < setup süresi + 1 adetin üretim süresi (2 saat 15 dk) ise o hafta üretim durur. |


## B.4 Haftanın akışı

Her hafta, her ürün için sırasıyla:

1. **Pazartesi:** stoklara bakılır, basit kural üretim kararını verir.
2. **Üretim:** üretilen miktar stoğa eklenir. Bu hafta üretilen parça bu hafta sevk edilebilir (CLSP varsayımı, Tempelmeier 2013).
3. **Talep:** rastgele talep çekilir, stoktan düşülür. Stok negatife inerse eksi kısım bekleyen siparişlerdir.
4. **Hafta sonu maliyet:**
   - Setup: yapılan setup sayısı × 300 $
   - Stok maliyeti: stok > 0 ise stok × h
   - Gecikme cezası: stok < 0 ise |stok| × ceza

12 haftanın toplam maliyeti = 1 run.

## B.5 Açık konular

- [ ] Her sayının kaynağı: talepler, süreler, maliyetler, başlangıç stokları (kitapçık 1.1)

