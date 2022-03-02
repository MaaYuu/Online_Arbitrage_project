$path_oa = "C:\Users\Mahmut\Desktop\Online_Arbitrage\online_arbitrage"
$path_cs = "C:\Users\Mahmut\Desktop\Online_Arbitrage\online_arbitrage_files\ciceksepeti"
$path_et = "C:\Users\Mahmut\Desktop\Online_Arbitrage\online_arbitrage_files\etsy\"
$file_cs = Get-ChildItem -Path $path_cs -Force -Recurse -File | Select-Object -First 1
$file_et = Get-ChildItem -Path $path_et -Force -Recurse -File | Select-Object -First 1
$file_et = $path_et + $file_et
$img_path = "C:\\Users\Mahmut\\Desktop\\Online_Arbitrage\\online_arbitrage_files\\etsy_images\\"


# &Set-Location $path_oa
# &c:/Users/Mahmut/Desktop/Online_Arbitrage/arbitrage_venv/Scripts/Activate.ps1
# &scrapy crawl ciceksepeti -a kategori='TakiSaatAksesuar' -a fiyat='Max100' -a siralama='Degerlendirilen'
# &Start-Sleep -s 2
# &scrapy crawl etsy
# &Set-Location $path_cs
# &Move-Item -Path $file_cs -Destination "../Archives"
# &Set-Location $path_oa
&python image_download.py $file_et $img_path
# &Start-Sleep -s 10



# EvYasam,2007147 -> Ev Yaşam
# HediyeSetleri,2014253 -> Hediye Setleri
# Hediyelik,2009384 -> Hediyelik
# Hobi, 2008680 -> Hobi
# Kits, 2089408 -> Kits
# Kozmetik, 2009388 -> Kozmetik
# Moda, 2009385 -> Moda
# HediyeSetleri8, 2121501 -> Hediye Setleri 8
# OfisKirtasiye ,2008044 -> Ofis Kırtasiye
# OtoAksesuar ,2009386 -> Oto Aksesuar
# Oyuncak ,2009387 -> Oyuncak
# SporOutdoor ,2008662 -> Spor-Outdoor
# TakiSaatAksesuar,2009390 -> Takı, saat, aksesuar
# KisiyeOzel ,2007217 -> Kişiye Özel

# https://www.ciceksepeti.com/tum-urunler?df=2007101,2009386,2009390

# Fiyat
# &priceId=
# Max50,  0-50 TL -> 1
# Max100, 50-100 TL-> ,2
# Max150, 100-150 TL-> ,3
# Max200, 150-200 TL-> ,4
# Max250, 200-250 TL-> ,5
# Max500, 250-500 TL-> ,6
# Max1000, 500-1000TL-> ,7
# Min1000, 1000 TL üst->,8


# Sıralama
# &orderby=
# Degerlendirilen=8
# Yeni=9
# Begenilen=7
# Ucuz=3
# Pahalı=2
# CokSatilan=1
