| Factor                 | RSA-2048                                | ECC-P256 (secp256r1)                                    |
| ---------------------- | --------------------------------------- | ------------------------------------------------------- |
| **Key size**           | Large (public: 256B, private: \~2KB)    | Small (pub: 64B, priv: 32B)                             |
| **Key generation**     | Slow (100ms+)                           | Very fast (sub-ms)                                      |
| **Enc/Dec speed**      | Similar (AES dominates)                 | Similar (AES dominates)                                 |
| **Computational cost** | High (big integer math)                 | Low (elliptic curve math)                               |
| **Security margin**    | Well-studied, but vulnerable to quantum | Smaller keys, more efficient, but same quantum weakness |
| **Storage overhead**   | Larger certificates                     | Smaller, better for IoT/mobile                          |
| **Best use case**      | Legacy, compatibility-heavy systems     | Modern secure file transfer, IoT, mobile                |
