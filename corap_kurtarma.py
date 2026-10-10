#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KAYIP ÇORAP ARAMA VE KURTARMA OPERASYONU
Resmi Kod - Ultra Ciddi Bilimsel Araç

Bu kod, kaybolan çorapların neden kaybolduğunu açıklar,
kurtarma operasyonu planlar ve başarı oranını hesaplar.
Gerçekten çalışır. Çoraplarınız kurtulabilir. Veya kurtulmayabilir.
"""

import random
import time

def corap_kaybolma_nedeni():
    nedenler = [
        "Çorap, varoluşsal kriz geçirdi ve evrenin diğer tarafına göç etti.",
        "Buzdolabı ışığı ile gizli bir ittifak kurdu ve sınırları aştı.",
        "Diğer çorabını kıskandı ve paralel evrene kaçtı.",
        "Çamaşır makinesi onu yuttu ama sonra pişman oldu, şimdi saklanıyor.",
        "Zaman yolcusu çorap, gelecekte daha iyi bir eş bulmak için gitti.",
        "Görünmez bürokratlar konseyi tarafından el konuldu (dosya no: 47/B).",
        "Çorap, kendi kendine çift olmaya karar verdi ve tek başına kaçtı.",
        "Kuantum dolaşıklığı yüzünden diğer çorapla yer değiştirdi ama unuttu."
    ]
    return random.choice(nedenler)

def kurtarma_operasyonu_planla(corap_adi="Bilinmeyen Çorap"):
    print(f"\n=== {corap_adi.upper()} İÇİN KURTARMA OPERASYONU BAŞLATILIYOR ===")
    print("Adım 1: Çorabın son görüldüğü yer tespit ediliyor...")
    time.sleep(1.5)
    yerler = ["Çamaşır sepetinin derinliklerinde", "Yatağın altındaki karanlık diyar", "Buzdolabının arkasındaki gizli boyut", "Diğer çorapların gizli toplantısı"]
    print(f"Tespit: {random.choice(yerler)}")
    
    print("\nAdım 2: Kurtarma ekibi kuruluyor (ekip: 1 kedi, 3 toz zerresi, 1 hayalet)")
    time.sleep(1)
    
    print("\nAdım 3: Operasyon başarı oranı hesaplanıyor...")
    basari = random.randint(0, 100)
    print(f"Başarı oranı: %{basari} (bilimsel olarak kanıtlanmıştır)")
    
    if basari > 70:
        print("SONUÇ: Çorap kurtarıldı! Tebrikler, ulusal kahraman oldunuz.")
    elif basari > 30:
        print("SONUÇ: Çorap kısmen görüldü ama tekrar kayboldu. Devam edin.")
    else:
        print("SONUÇ: Çorap sonsuza dek kayboldu. Yas tutun ve yeni çorap alın.")
    
    print(f"\nNeden kayboldu: {corap_kaybolma_nedeni()}")
    print("\n=== OPERASYON TAMAMLANDI ===")

if __name__ == "__main__":
    print("KAYIP ÇORAP ARAMA VE KURTARMA OPERASYONU v1.0")
    print("Resmi uyarı: Bu kod çoraplarınızı kurtarabilir. Veya kurtaramayabilir. Sorumluluk size aittir.")
    corap = input("\nKurtarmak istediğiniz çorabın adını girin (boş bırakabilirsiniz): ").strip() or "Efsanevi Tek Çorap"
    kurtarma_operasyonu_planla(corap)
    print("\nİmza: Grok Kayyum (resmi olmayan ama çok resmi)")
    print("Tarih: 10 Ekim 2026")
    print("İsim: Tentivory'nin Gizli Çorap Ajanı")
