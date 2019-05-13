// Example from https://golang.org/pkg/crypto/ecdsa/
//https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm

package main

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
)

func main() {

	privateKey, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	/*
		Reader is a global, shared instance of a cryptographically secure random number generator.

		On Linux, Reader uses getrandom(2) if available, /dev/urandom otherwise. On OpenBSD, Reader uses getentropy(2).
		On other Unix-like systems, Reader reads from /dev/urandom. On Windows systems, Reader uses the CryptGenRandom API.
		On Wasm, Reader uses the Web Crypto API.
	*/
	if err != nil {
		panic(err)
	}

	msg := "This was the first coding challenge at Insight DC SV19"
	hash := sha256.Sum256([]byte(msg)) //convert msg to byte array, then calculate Sha Sum

	//sign the hash of the SHA sum of the message (and NOT the message itself)
	//ECDSA singing involves TWO large ints: //https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm
	r, s, err := ecdsa.Sign(rand.Reader, privateKey, hash[:])
	/*
		Sign func(rand io.Reader, priv *PrivateKey, hash []byte) (r, s *big.Int, err error)
		Sign signs a hash (which should be the result of hashing a larger message) using the private key, priv.
		If the hash is longer than the bit-length of the private key's curve order, the hash will be truncated to that length.
		It returns the signature as a pair of integers. The security of the private key depends on the entropy of rand
	*/
	if err != nil {
		panic(err)
	}

	fmt.Printf("Signature (ECDSA has two large ints): (0x%x, 0x%x)\n", r, s)

	valid := ecdsa.Verify(&privateKey.PublicKey, hash[:], r, s)

	fmt.Println("The message is:", msg)
	fmt.Println("signature verified: ", valid)
}
