# Input dari user
total_belanja_1005 = float(input("Masukkan total belanja (Rp): "))

# Input dari status member ( mengecek apakah user mengetik 'y' atau 'ya')
input_member_1005 = input("Apakah anda member (y/t): ").strip().lower()
is_member_1005 = input_member_1005 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1005 = input ("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1005 = input_promo_1005 in["y", "ya"]

total_diskon_persen_1005 = 0

if total_belanja_1005 > 1000000:
    total_diskon_persen_1005 += 10 #Diskon belanja besar

if is_member_1005:
    total_diskon_persen_1005 += 5 #Diskon member

if kode_promo_valid_1005:
    total_diskon_persen_1005 += 15 #Diskon Voucher

#Menghitung nominal diskon dan total bayar
nominal_diskon_1005 = total_belanja_1005 * (total_diskon_persen_1005 /100)
total_bayar_1005 = total_belanja_1005 - nominal_diskon_1005

#Output hasil
print("/n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_1005}% (Rp{nominal_diskon_1005:,.0f})")
print(f"Total Bayar : Rp {total_bayar_1005: ,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_1005}%")
# Output total diskon yang anda dapatkan : 30% jika belanja > 1juta, member, dan kode promo valid