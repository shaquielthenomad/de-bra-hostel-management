# 🏨 De Bra Hostel Management System

> **Comprehensive hostel management solution for De Bra Hostel @ Koh Lanta, Thailand**

A complete ERP system built on Frappe/ERPNext with custom hostel management features including room booking, motorcycle rentals, volunteer management, and guest services.

## 🌟 Features

### 🏠 **Room Management**
- 6-bed mixed dorms (Room 4 & 5)
- 6-bed female-only dorm (Room 3)  
- Private rooms with queen beds
- Private rooms with full kitchen
- Real-time availability checking
- Automated pricing and booking

### 🏍️ **Motorcycle Rental System**
- **15+ motorcycles** from 125cc scooters to 750cc big bikes
- Honda Click 125cc, Yamaha Nmax 155cc, Honda PCX 150cc
- Kawasaki Ninja 300, Honda CB500F, Kawasaki Z650
- Comprehensive rental forms with safety agreements
- Insurance and safety equipment tracking
- Digital contracts and liability waivers

### 👥 **Volunteer Management**
- Online volunteer applications with personality screening
- Skills-based matching (reception, housekeeping, coffee shop, etc.)
- Work hour tracking and accommodation credits
- Achievement system and recognition program
- Scheduling and shift management

### ☕ **Additional Services**
- Coffee shop with barista training tracking
- Convenience store inventory management
- Guest tab system (charge to room)
- Laundry service scheduling
- Airport pickup coordination

### 💳 **Payment & Booking**
- Multi-currency support (THB, USD, EUR, etc.)
- Cash, card, bank transfer, PayPal integration
- Guest tab system for convenience
- Automated invoicing and receipts

## 🚀 Quick Deploy to Railway

### One-Click Deployment
1. **Fork this repository** to your GitHub account
2. **Go to [Railway.app](https://railway.app)** and sign up/login with GitHub
3. **Click "Deploy from GitHub repo"** and select this repository
4. **Railway will automatically**:
   - Detect configuration from `railway.json`
   - Install Python dependencies from `requirements.txt`
   - Run `setup_railway.py` to initialize ERPNext
   - Provision PostgreSQL database and Redis
   - Start the web server

### 🎯 What You Get
- **Live ERPNext Dashboard**: Complete business management
- **Room Booking System**: 6 room types with availability checking
- **Motorcycle Fleet**: 15+ bikes with rental management
- **Volunteer System**: Applications, scheduling, recognition
- **API Endpoints**: RESTful APIs for all features
- **Database**: PostgreSQL with Redis caching

## 🏗️ Project Structure

```
de-bra-hostel-management/
├── 📄 railway.json              # Railway deployment config
├── 📄 requirements.txt          # Python dependencies
├── 📄 setup_railway.py          # Railway initialization script
├── 📄 package.json              # Node.js package info
├── 📄 frappe_app.py             # Flask web application
├── 📄 RAILWAY-DEPLOYMENT.md     # Detailed deployment guide
├── 📁 frappe-bench/
│   ├── 📁 custom-forms/
│   │   ├── bike-rental-form.js      # 🏍️ Comprehensive bike rental
│   │   └── guest-checkin-form.js    # 🏨 Guest registration
│   ├── 📁 src/
│   │   ├── index.js                 # 🌐 Main Cloudflare Workers app
│   │   └── volunteer-system.js      # 👥 Volunteer management
│   └── 📁 sites/
│       ├── mysite.local/            # Development site
│       └── test.local/              # Testing site
├── 📁 sites/
│   ├── apps.txt                     # Installed apps list
│   └── RAILWAY-DEPLOYMENT.md       # Deployment documentation
└── 📁 logs/                         # Application logs
```

## 🔧 Technical Stack

- **Backend**: ERPNext 14.x on Frappe Framework
- **Frontend**: Cloudflare Workers with responsive design
- **Database**: PostgreSQL (Railway managed)
- **Cache**: Redis (Railway managed)
- **Deployment**: Railway with automatic scaling
- **Languages**: Python 3.8+, JavaScript ES6+

## 🏨 Hostel Specific Features

### Room Types & Pricing
| Room Type | Capacity | Rate (THB/night) | Features |
|-----------|----------|------------------|----------|
| 6-Bed Mixed Dorm (Room 4) | 6 | ฿285 | A/C, Garden view, Ensuite |
| 6-Bed Female Dorm (Room 3) | 6 | ฿285 | Female-only, Kitchen, A/C |
| Private Queen Room | 2 | ฿636 | Queen bed, Mountain view |
| Private with Kitchen | 2 | ฿750 | Full kitchen, Garden view |

### Motorcycle Fleet
| Category | Models | Rate Range | Features |
|----------|--------|------------|----------|
| **Scooters** | Honda Click 125cc, Yamaha Nmax 155cc | ฿200-250/day | Automatic, beginner-friendly |
| **Street Bikes** | Honda CB150R | ฿350/day | Manual transmission |
| **Sport Bikes** | Kawasaki Ninja 300 | ฿500/day | Performance riding |
| **Big Bikes** | Honda CB500F, Kawasaki Z650 | ฿600-750/day | Advanced riders only |

## 🌐 API Endpoints

### Room Management
- `GET /api/rooms` - Get room availability
- `POST /api/booking` - Create new booking
- `POST /api/checkin` - Guest registration

### Motorcycle Rentals
- `GET /api/bike-rental` - Check bike availability
- `POST /api/bike-rental` - Create rental booking

### Volunteer System
- `POST /api/volunteer/apply` - Submit application
- `GET /api/volunteer/schedule` - Get volunteer schedule
- `POST /api/volunteer/hours` - Log work hours

### Business Management
- `GET /api/admin/dashboard` - Admin dashboard data
- `GET /api/admin/revenue` - Revenue analytics
- `POST /api/admin/sync-erpnext` - Sync with ERPNext

## 📱 Features by User Type

### 🏨 **For Guests**
- Online room booking with instant confirmation
- Digital check-in forms with policy agreements
- Motorcycle rental with safety briefings
- Guest tab system for convenient payments
- Service requests and feedback

### 👥 **For Volunteers**
- Personality-based application system
- Skills matching and work scheduling
- Hour tracking with accommodation credits
- Achievement system and recognition
- Community features and events

### 🏢 **For Management**
- Complete ERP dashboard with analytics
- Inventory management for bikes and supplies
- Revenue tracking and financial reports
- Staff scheduling and payroll integration
- Customer relationship management

## 🔒 Security & Compliance

- **Data Protection**: Guest information encrypted and secured
- **Privacy Compliance**: GDPR-compliant data handling
- **Payment Security**: PCI-compliant payment processing
- **Access Control**: Role-based permissions system
- **Audit Trail**: Complete transaction logging

## 🌍 Localization

- **Multi-language**: Thai, English, Swedish, German
- **Multi-currency**: THB, USD, EUR, SEK, NOK
- **Local Integration**: Thai banking and payment systems
- **Cultural Adaptation**: Local business practices

## 📈 Scalability

- **Cloud-Native**: Designed for Railway and cloud platforms
- **Auto-Scaling**: Handles traffic spikes automatically
- **Database Optimization**: Efficient queries and caching
- **CDN Integration**: Fast global content delivery
- **Microservices Ready**: Modular architecture

## 🤝 Contributing

This system is specifically designed for De Bra Hostel operations but can be adapted for other hostels:

1. Fork the repository
2. Modify configurations for your hostel
3. Update room types, pricing, and services
4. Deploy to your preferred platform

## 📞 Support

- **Technical Support**: [GitHub Issues](https://github.com/shaquielthenomad/de-bra-hostel-management/issues)
- **Business Inquiries**: debrahostel@gmail.com
- **Emergency Contact**: +66 62 221 5910

## 📄 License

MIT License - Feel free to adapt for your hostel needs.

---

**🏝️ Built with ❤️ for De Bra Hostel @ Koh Lanta, Thailand**

*Creating amazing experiences for travelers while supporting local communities through volunteer programs and sustainable tourism.* 