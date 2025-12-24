# Simple Single Sign-On (SSO) Authorization System  
### Using JWT and RSA Digital Signatures

---

## Overview

This repository (**Repository 1**) contains a foundational implementation of a **Single Sign-On (SSO) authorization system** built using **JSON Web Tokens (JWT)** and **RSA-based digital signatures**.

The project is intentionally scoped to demonstrate **core Identity and Access Management (IAM) and cryptographic principles** without introducing advanced trust models or adversarial scenarios. It serves as a **baseline SSO system**, against which more advanced mechanisms and attack analyses can be evaluated.

---

## Purpose of the Project

The purpose of this repository is to:

- Understand how Single Sign-On operates at a foundational level  
- Implement stateless authorization using JWT  
- Apply RSA digital signatures (RS256) for token authenticity  
- Clearly distinguish between hashing, encryption, and signing  
- Establish a clean reference implementation for further IAM experimentation  

This repository prioritizes **correctness, clarity, and architectural minimalism**.

---

## Key Concepts Covered

- Single Sign-On (SSO)
- Authentication vs Authorization
- JSON Web Tokens (JWT)
- JWT structure (Header, Payload, Signature)
- RSA public-key cryptography
- SHA-256 hashing
- Digital signatures
- Stateless authorization
- Trust assumptions in distributed systems

---

## Cryptography at a Glance

| Component | Purpose | Algorithm |
|--------|--------|---------|
| Token Integrity | Detect tampering | SHA-256 |
| Token Authenticity | Verify issuer | RSA (RS256) |
| Transport Security | Encrypt communication | AES-256 (via HTTPS/TLS) |

Note: AES-256 is not used in JWT creation or signing. It is used implicitly at the transport layer to protect data in transit.

---

## High-Level Architecture

- **Client**  
  Uses a JWT to access protected resources  

- **Authentication Server**  
  Issues digitally signed JWTs  

- **Resource Server**  
  Verifies token signatures and claims before granting access  

The system is stateless and does not rely on server-side session storage.

---

## Authorization Flow (Simplified)

1. User authenticates with the authentication server  
2. Server generates a JWT  
3. JWT is signed using the RSA private key  
4. Token is returned to the client  
5. Client includes the JWT in API requests  
6. Resource server verifies the signature using the public key  
7. Token claims are validated  
8. Access is granted or denied  

---

## Security Properties

### Addressed in Repository 1

- Token tampering  
- Token forgery  
- Unauthorized token issuance  
- Replay attacks (limited via expiration claims)  

### Trust Assumptions

This implementation assumes:
- A trusted authentication server  
- Secure key management for the RSA private key  
- HTTPS is enforced for all communications  

These assumptions are explicitly documented to maintain conceptual clarity.

---

## Known Limitations

This repository intentionally does not implement:

- Certificate-based trust validation  
- Refresh tokens or token revocation  
- Key rotation mechanisms  
- Role-Based Access Control (RBAC)  
- OAuth 2.0 / OpenID Connect compliance  
- Audit logging  
- Adversarial attack simulations  

These exclusions are deliberate and define the boundary of this repository.

---

## Relationship to Repository 2

This repository represents the baseline SSO design.

A second repository (Repository 2) builds upon this foundation by introducing progressively advanced concepts:

- **Feature 1:** Analysis and demonstration of attacks that exploit simplistic SSO and JWT-based authorization designs  
- **Feature 2:** Certificate-based trust, validation mechanisms, and improved key management  

This progression follows a security-first methodology, where weaknesses are first identified and analyzed, and then systematically mitigated using stronger trust and validation models.

Separating these concerns allows this repository to remain minimal and conceptually clear, while enabling deeper exploration of real-world IAM challenges in a dedicated extension.


## Documentation

A detailed technical report explaining:

- JWT internals  
- RSA vs SHA-256 vs AES-256  
- System architecture  
- Authorization flow  
- Security analysis and limitations  

is available here:

[Detailed Technical Report (PDF)](docs/SSO_Authorization_JWT_RSA_Technical_Report.pdf)


This README provides a high-level overview.  
The linked document is the authoritative technical reference.

---

## Learning Outcomes

- Practical understanding of JWT-based authorization  
- Correct application of RSA digital signatures  
- Clear separation of cryptographic responsibilities  
- Foundational IAM system design knowledge  
- Ability to reason about trust boundaries and limitations  

---

## Installation and Setup

This project is intended for educational and experimental use.  
The following steps describe how to set up and run the project locally.

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment support (`venv`)

---

### Setup Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/simple_sso_token_auth.git
cd simple_sso_token_auth
```
#### 2. Create and Activate a Virtual Environment

Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Install Dependencies
If a requirements.txt file is present, install all required packages using:
```bash
pip install -r requirements.txt
```
Typical dependencies for this project include:

A lightweight web framework (e.g., Flask)

A JWT handling library

A cryptography library for RSA operations

#### 3. Install Dependencies
Start the Application or Authentication Server using:
```bash
python app.py
```
The server will start locally and expose endpoints for authentication and token-based authorization.

## Disclaimer

This repository is educational and foundational in nature.  
It is not intended for production use without additional security hardening, testing, and compliance measures.

---

## Author

**Ramesh Harisabapathi Chettiar**  
Undergraduate Student – Cybersecurity / Computer Science  
Focus Areas: IAM, Cloud Security, Applied Cryptography  

---

## References

- RFC 7519 – JSON Web Token (JWT)  
- RFC 7515 – JSON Web Signature (JWS)  
- NIST Cryptographic Standards  
- TLS / HTTPS Documentation  
