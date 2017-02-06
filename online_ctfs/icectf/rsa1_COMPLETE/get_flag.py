# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-12 14:27:57
# @Last Modified by:   john
# @Last Modified time: 2016-08-25 17:58:10

import binascii

n=0x180be86dc898a3c3a710e52b31de460f8f350610bf63e6b2203c08fddad44601d96eb454a34dab7684589bc32b19eb27cffff8c07179e349ddb62898ae896f8c681796052ae1598bd41f35491175c9b60ae2260d0d4ebac05b4b6f2677a7609c2fe6194fe7b63841cec632e3a2f55d0cb09df08eacea34394ad473577dea5131552b0b30efac31c59087bfe603d2b13bed7d14967bfd489157aa01b14b4e1bd08d9b92ec0c319aeb8fedd535c56770aac95247d116d59cae2f99c3b51f43093fd39c10f93830c1ece75ee37e5fcdc5b174052eccadcadeda2f1b3a4a87184041d5c1a6a0b2eeaa3c3a1227bc27e130e67ac397b375ffe7c873e9b1c649812edcd
e=0x1
c=0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d


# Since E is 1, that means that D is 1 as well (because D = E ** -1 * mod(N))
#

# The encryption function is pow( c, e, n ) ...or... (c ** e ) % n
# Having an e to the power of one means you haven't encrypted anything
# It is just simply modular 
decrypted = hex(c)[2:-1]
# print decrypted
print binascii.unhexlify(decrypted)