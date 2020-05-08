On one of the tutorials, we discussed what was called the Stargate Ghost Problem. The problem goes like this:

Suppose you just entered a Stargate and you traveled to another planet. An alien came back with you in human form but you found out that you were invisible to others. You need to speak to you r commanding officer but you can only communicate through the alien.

How would you communicate to your commanding officer through the alien as an interpreter securely?

This presents a number of challenges:
* Surely, you can't trust an alien you just met.
* How can you communicate to your commanding officer through an untrusted medium?
* What if the alien alters the message?

We are looking for a number of security properties:
* Integrity - The message you send must be unaltered by the alien, and must be received by the commanding officer.
* Confidentiality - Messages must be private between.
* Authenticity - The commanding officer needs to know he is communicating with the right person.
* (Optional) Forward Secrecy - Any communication between you and the major should be difficult to recreate again in the future.


For integrity:
Some sort of Message Authentication Code could work. Every time a message is transmitted, the alien must say the hash (last few characters to make it easy to say?) of the message.

However this is susceptible to length extension attack. The alien can just extend the message and calculate a new hash.

An HMAC could work better but it is more complicated to calculate with more keys required. How would you also share the key?

For authenticity:
Personal questions can be asked by the commanding officer to verify your identity.

You can also ask the alien to have yourself and the officer on a separate room in private. Come up with a yes/no codeword to confirm if you are who you say your are. For example, let the alien say "bread" in a sentence you are actually him.

For confidentiality:
A symmetric key encryption could work if there was some pre-shared secret before. If you and the commanding officer came up with a protocol before entering the stargate, secret codes can be used to denote positive / negative responses. Secret code words can also be given.

However, given the situation, it may not be possible to pre-share a secret.

A Diffie-Hellman Key Agreement (in theory) could work really well for this situation. This protocol can enable two parties to generate the same symmetric key without transmitting the actual key for communication. 

This works by modulo arithmetic where Party A and Party B initially share publicly known numbers. These numbers would be used to generate private keys in secret. They generate (and most imporatantly keep) the private key themselves.

However, this requires mathematically intensive calculations which may not be suitable for verbal communication. The alien might just give up and sense some plot to destroy his home planet and refuse to cooperate.

The Diffie-Hellman Key Exchange can also be susceptible to a man-in-the-middle attack. The alien could alter the key-exchange in the beginning. He could trick Party A and B to think they are exchanging the generator numbers, but in fact, the alien is in the middle trying to generate two Diffie-Hellman Key Exchanges. The alien could intercept and read the messages in between.

When it all else fails, just go for the good old social engineering attack. Trick the alien you are on his side.