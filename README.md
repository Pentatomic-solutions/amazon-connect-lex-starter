# Amazon Connect & Lex Conversational IVR Quickstart Blueprint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AWS Provider](https://img.shields.io/badge/AWS-Amazon%20Connect%20%7C%20Lex%20V2-232F3E?logo=amazon-aws)](https://aws.amazon.com/connect/)
[![Maintained by Pentatomic Solutions](https://img.shields.io/badge/Maintained%20by-Pentatomic%20Solutions-blue)](https://pentatomicsolutions.in/amazon-connect-consulting-services/)

Enterprise cloud contact center architecture blueprint for deploying **Amazon Connect** with **Amazon Lex V2** conversational IVR, serverless **AWS Lambda** CRM data lookups, and **Contact Lens** speech analytics.

Architected by [Pentatomic Solutions](https://pentatomicsolutions.in) — Specialists in enterprise contact center migrations and cloud software engineering.

---

## Architecture Overview

```
                                    +--------------------------------+
                                    |  Customer Inbound Interaction  |
                                    |     (PSTN / DID / WebRTC)      |
                                    +----------------+---------------+
                                                     |
                                                     v
                                    +----------------+---------------+
                                    |      Amazon Connect Core       |
                                    |       Telephony Engine         |
                                    +----------------+---------------+
                                                     |
                         +---------------------------+---------------------------+
                         |                                                       |
                         v                                                       v
        +----------------+---------------+                      +----------------+---------------+
        |   Amazon Lex V2 Conversational |                      |   AWS Lambda Sub-Second        |
        |   Natural Language IVR Bot     | <------------------> |   CRM Data Connectors          |
        |   (Intent Recognition & OTP)   |                      |   (Salesforce, Zendesk, DB)    |
        +--------------------------------+                      +--------------------------------+
                         |
                         v
        +----------------+---------------+
        |  Amazon Connect Contact Lens   |
        |  Real-Time Sentiment & Audio   |
        +----------------+---------------+
                         |
                         v
        +----------------+---------------+
        |  Agent Workspace (CCP) with    |
        |  Caller Screen-Pop Data        |
        +--------------------------------+
```

---

## Features Included

- **Zero-Downtime PBX Migration Pattern**: Dual-routing configuration for phased cutovers from Avaya Aura, Cisco CUCM, or Genesys.
- **Conversational Lex V2 Flow**: Pre-built slots, intents, and fallback handlers for customer account verification and routing deflection.
- **Sub-Second Lambda Integration**: Serverless Python / Node.js handlers configured with connection pooling for real-time CRM API lookups.
- **Contact Lens Configuration**: Sentiment thresholds, conversational keyword triggers, and supervisor real-time alerts.
- **CloudFormation / CDK Templates**: Infrastructure-as-Code (IaC) deployment for AWS telephony instances and routing profiles.

---

## Deployment & Quickstart

```bash
# Clone repository
git clone https://github.com/pentatomic-solutions/amazon-connect-lex-starter.git
cd amazon-connect-lex-starter

# Deploy via AWS CDK
npm install
cdk bootstrap
cdk deploy --parameters ConnectInstanceAlias=penta-prod-contact-center
```

---

## Commercial Consulting & Migration Support

Need enterprise migration planning, custom CRM screen-pop engineering, or 24/7 SLA operational support?
- **Pillar Guide**: [Amazon Connect Consulting Services](https://pentatomicsolutions.in/amazon-connect-consulting-services/)
- **Technical Inquiries**: contact@pentatomicsolutions.in
- **Direct WhatsApp**: [+91 93168 17687](https://wa.me/919316817687)
