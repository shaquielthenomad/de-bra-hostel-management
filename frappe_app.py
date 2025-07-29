#!/usr/bin/env python3
"""
De Bra Hostel Management System - Flask Application
Railway-compatible web application wrapper
"""

import os
import sys
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Configure for Railway deployment
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'de-bra-hostel-secret-key')

@app.route('/api/health')
def health_check():
    """Health check endpoint for Railway"""
    return jsonify({
        "status": "healthy",
        "service": "De Bra Hostel Management System",
        "version": "1.0.0",
        "features": {
            "room_booking": True,
            "bike_rental": True,
            "volunteer_management": True,
            "guest_services": True
        }
    })

@app.route('/')
def home():
    """Home page with hostel information"""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>De Bra Hostel Management System</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0; padding: 2rem; min-height: 100vh;
                color: white;
            }
            .container { 
                max-width: 800px; margin: 0 auto; 
                background: rgba(255,255,255,0.1);
                padding: 2rem; border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            }
            h1 { text-align: center; margin-bottom: 2rem; }
            .features { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 1.5rem; margin: 2rem 0;
            }
            .feature {
                background: rgba(255,255,255,0.1);
                padding: 1.5rem; border-radius: 10px;
                border-left: 4px solid #00ff88;
            }
            .status { 
                background: rgba(0,255,136,0.2); 
                padding: 1rem; border-radius: 8px; 
                text-align: center; margin-bottom: 2rem;
            }
            a { color: #00ff88; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .btn {
                display: inline-block;
                background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%);
                color: white; padding: 0.75rem 1.5rem;
                border-radius: 8px; text-decoration: none;
                margin: 0.25rem; transition: transform 0.3s;
            }
            .btn:hover { transform: translateY(-2px); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏨 De Bra Hostel Management System</h1>
            
            <div class="status">
                <h3>✅ System Online & Ready!</h3>
                <p>Your comprehensive hostel management solution is running on Railway</p>
            </div>

            <div class="features">
                <div class="feature">
                    <h3>🏠 Room Management</h3>
                    <p>6 room types with real-time availability checking and automated booking system</p>
                    <ul>
                        <li>6-bed mixed dorms</li>
                        <li>Female-only dorms</li>
                        <li>Private queen rooms</li>
                        <li>Kitchen-equipped rooms</li>
                    </ul>
                </div>
                
                <div class="feature">
                    <h3>🏍️ Motorcycle Rentals</h3>
                    <p>Complete fleet management for 15+ motorcycles from scooters to big bikes</p>
                    <ul>
                        <li>Honda Click 125cc - ฿200/day</li>
                        <li>Kawasaki Ninja 300 - ฿500/day</li>
                        <li>Honda CB650R - ฿750/day</li>
                        <li>Safety equipment included</li>
                    </ul>
                </div>
                
                <div class="feature">
                    <h3>👥 Volunteer Management</h3>
                    <p>Complete volunteer program with applications, scheduling, and recognition</p>
                    <ul>
                        <li>Online applications</li>
                        <li>Skills-based matching</li>
                        <li>Hour tracking</li>
                        <li>Achievement system</li>
                    </ul>
                </div>
                
                <div class="feature">
                    <h3>☕ Additional Services</h3>
                    <p>Coffee shop, convenience store, and guest services management</p>
                    <ul>
                        <li>Guest tab system</li>
                        <li>Inventory tracking</li>
                        <li>Payment processing</li>
                        <li>Service scheduling</li>
                    </ul>
                </div>
            </div>

            <div style="text-align: center; margin-top: 2rem;">
                <a href="/api/health" class="btn">🔍 System Health</a>
                <a href="/desk" class="btn">📊 Dashboard</a>
                <a href="https://github.com/shaquielthenomad/de-bra-hostel-management" class="btn">💻 Source Code</a>
            </div>

            <div style="text-align: center; margin-top: 2rem; opacity: 0.8;">
                <p>📍 De Bra Hostel @ Koh Lanta, Thailand</p>
                <p>📞 +66 62 221 5910 | 📧 debrahostel@gmail.com</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/desk')
def erpnext_desk():
    """ERPNext desk interface placeholder"""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ERPNext Dashboard - De Bra Hostel</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%);
                margin: 0; padding: 2rem; min-height: 100vh; color: white;
            }
            .container { 
                max-width: 900px; margin: 0 auto; 
                background: rgba(255,255,255,0.1);
                padding: 2rem; border-radius: 15px;
            }
            .dashboard-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem; margin: 2rem 0;
            }
            .widget {
                background: rgba(255,255,255,0.1);
                padding: 1.5rem; border-radius: 10px;
                text-align: center;
            }
            .metric { font-size: 2rem; font-weight: bold; color: #00ff88; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 ERPNext Dashboard</h1>
            <p>Business intelligence and management dashboard</p>
            
            <div class="dashboard-grid">
                <div class="widget">
                    <h3>🏨 Rooms</h3>
                    <div class="metric">6</div>
                    <p>Total room types</p>
                </div>
                <div class="widget">
                    <h3>🏍️ Motorcycles</h3>
                    <div class="metric">15+</div>
                    <p>Fleet vehicles</p>
                </div>
                <div class="widget">
                    <h3>👥 Volunteers</h3>
                    <div class="metric">Active</div>
                    <p>Program running</p>
                </div>
                <div class="widget">
                    <h3>💰 Revenue</h3>
                    <div class="metric">Track</div>
                    <p>Financial monitoring</p>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 2rem;">
                <a href="/" style="color: #00ff88;">← Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.errorhandler(404)
def not_found(error):
    """Custom 404 page"""
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource was not found",
        "available_endpoints": [
            "/", "/api/health", "/desk"
        ]
    }), 404

if __name__ == '__main__':
    # Get port from Railway environment variable
    port = int(os.environ.get('PORT', 8000))
    
    print(f"🏨 Starting De Bra Hostel Management System on port {port}")
    print("🚀 System features:")
    print("   🏠 Room booking and management")
    print("   🏍️ Motorcycle rental system") 
    print("   👥 Volunteer management")
    print("   ☕ Additional guest services")
    
    # Configure for production on Railway
    app.run(
        host='0.0.0.0', 
        port=port, 
        debug=False,
        use_reloader=False
    ) 