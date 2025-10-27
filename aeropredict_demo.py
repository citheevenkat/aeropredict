#!/usr/bin/env python3
"""
AeroPredict - Live Demo Simulation
Demonstrates AI-powered predictive maintenance with real-time data
"""

import random
import time
from datetime import datetime, timedelta

class AeroPredictDemo:
    def __init__(self):
        self.engines = {
            1: {"health": 95, "risk": 12, "temp": 1650, "vibration": 3.2, "hours": 8420},
            2: {"health": 45, "risk": 89, "temp": 1847, "vibration": 8.2, "hours": 12340},
            3: {"health": 98, "risk": 8, "temp": 1620, "vibration": 2.8, "hours": 6200},
            4: {"health": 72, "risk": 34, "temp": 1720, "vibration": 5.1, "hours": 10100}
        }
        
    def print_header(self):
        print("\n" + "="*80)
        print("   🛫 AEROPREDICT - AI-POWERED PREDICTIVE MAINTENANCE DEMO")
        print("="*80 + "\n")
    
    def print_section(self, title):
        print(f"\n{'─'*80}")
        print(f"  {title}")
        print(f"{'─'*80}\n")
    
    def show_fleet_status(self):
        self.print_section("📊 FLEET STATUS DASHBOARD")
        
        print("  ┌─────────────────────────────────────────────────────┐")
        print("  │  Total Aircraft: 50        Operational: 48          │")
        print("  │  In Maintenance: 2         System Status: ✓ ONLINE  │")
        print("  │  Predictions Today: 10     Avg Lead Time: 45 days   │")
        print("  └─────────────────────────────────────────────────────┘")
        
    def show_engine_monitoring(self):
        self.print_section("🔍 ENGINE HEALTH MONITORING - Aircraft A320-001")
        
        for eng_num, data in self.engines.items():
            status = "🟢 NORMAL" if data["risk"] < 30 else "🟡 WARNING" if data["risk"] < 70 else "🔴 CRITICAL"
            
            print(f"  Engine #{eng_num}:")
            print(f"    Health Score: {data['health']}%  |  Failure Risk: {data['risk']}%  |  {status}")
            print(f"    Operating Hours: {data['hours']:,}  |  Temperature: {data['temp']}°F  |  Vibration: {data['vibration']} mm/s")
            print()
    
    def predict_failure(self, engine_num):
        self.print_section(f"🤖 AI PREDICTION - Engine #{engine_num}")
        
        engine = self.engines[engine_num]
        
        print("  ┌─ ML Model Analysis ──────────────────────────────────┐")
        print("  │                                                       │")
        print(f"  │  Component: High-Pressure Turbine Blade Assembly     │")
        print(f"  │  Failure Probability: {engine['risk']}%                          │")
        print(f"  │  Model Confidence: 89%                                │")
        print(f"  │  Predicted Failure: 15 days                           │")
        print("  │                                                       │")
        print("  │  Analysis Based On:                                   │")
        print(f"  │    • Temperature anomaly: {engine['temp']}°F (↑12%)         │")
        print(f"  │    • Vibration spike: {engine['vibration']} mm/s (↑156%)       │")
        print("  │    • Operating hours: 12,340 (approaching limit)     │")
        print("  │    • Historical patterns: Match to failure signature │")
        print("  │                                                       │")
        print("  └───────────────────────────────────────────────────────┘")
        
        print("\n  [✓] Prediction generated in 342ms")
        print("  [✓] Alert sent to maintenance system")
        print("  [✓] Automated workflow initiated...")
    
    def simulate_sensor_data(self, engine_num):
        self.print_section(f"📡 REAL-TIME SENSOR DATA - Engine #{engine_num}")
        
        print("  Collecting sensor readings...\n")
        
        sensors = [
            ("Temperature", f"{self.engines[engine_num]['temp']}°F", "🔴 ALERT"),
            ("Vibration", f"{self.engines[engine_num]['vibration']} mm/s", "🔴 ALERT"),
            ("Pressure", "42.3 psi", "🟢 NORMAL"),
            ("RPM", "15,240", "🟢 NORMAL"),
            ("Oil Temperature", "215°F", "🟢 NORMAL"),
            ("Fuel Flow", "2,340 lb/hr", "🟢 NORMAL"),
        ]
        
        for sensor, value, status in sensors:
            print(f"    {sensor:20s} : {value:15s}  {status}")
            time.sleep(0.3)
    
    def automate_response(self):
        self.print_section("⚡ AUTOMATED RESPONSE TIMELINE")
        
        steps = [
            ("AI Prediction Generated", "COMPLETE", "2 hours ago"),
            ("Parts Order Placed", "COMPLETE", "1 hour ago"),
            ("Maintenance Scheduled", "IN PROGRESS", "Just now"),
            ("Technician Notified", "IN PROGRESS", "Just now"),
        ]
        
        for i, (step, status, time_info) in enumerate(steps, 1):
            icon = "✓" if status == "COMPLETE" else "⏳"
            print(f"  {icon} Step {i}: {step:30s} [{status:11s}]  ({time_info})")
            time.sleep(0.5)
        
        print("\n  ┌─ Parts Order Details ────────────────────────────────┐")
        print("  │                                                       │")
        print("  │  Part Number: HPT-8472-A                              │")
        print("  │  Description: High-Pressure Turbine Blade Assembly    │")
        print("  │  Supplier: GE Aviation Parts                          │")
        print("  │  Cost: $4,200 (vs $12,600 rush order)                │")
        print("  │  Delivery: 5-7 business days                          │")
        print("  │  Status: ✓ Order Confirmed                            │")
        print("  │                                                       │")
        print("  └───────────────────────────────────────────────────────┘")
        
        print("\n  ┌─ Maintenance Schedule ───────────────────────────────┐")
        print("  │                                                       │")
        print("  │  Date: November 2, 2025 (10 days from now)            │")
        print("  │  Time: 1:00 AM - 7:00 AM (6 hour window)              │")
        print("  │  Technicians: 2 certified engineers assigned          │")
        print("  │  Aircraft Downtime: 6 hours (during layover)          │")
        print("  │  Flight Impact: ZERO cancellations                    │")
        print("  │                                                       │")
        print("  └───────────────────────────────────────────────────────┘")
    
    def show_cost_comparison(self):
        self.print_section("💰 COST SAVINGS ANALYSIS")
        
        print("  REACTIVE MAINTENANCE (Traditional):")
        print("    Emergency repair labor:           $18,000")
        print("    Rush parts (3x markup):            $12,600")
        print("    Aircraft downtime (48 hrs):        $15,400")
        print("    Flight cancellations (3 flights):   $6,000")
        print("    ────────────────────────────────────────────")
        print("    TOTAL COST:                        $52,000  🔴\n")
        
        print("  PREDICTIVE MAINTENANCE (AeroPredict):")
        print("    Planned maintenance labor:          $2,300")
        print("    Standard parts (normal price):      $4,200")
        print("    Aircraft downtime (6 hrs):              $0")
        print("    Flight cancellations:                   $0")
        print("    ────────────────────────────────────────────")
        print("    TOTAL COST:                         $6,500  🟢\n")
        
        print("  " + "="*50)
        print("    💵 SAVINGS: $45,500 per incident (89% reduction)")
        print("  " + "="*50)
    
    def show_monthly_impact(self):
        self.print_section("📈 MONTHLY PERFORMANCE SUMMARY")
        
        print("  Predictions This Month:")
        print("    • High Risk:     3 components")
        print("    • Medium Risk:   7 components")
        print("    • Low Risk:      190 components")
        print()
        print("  Prevented Failures: 12")
        print("  Total Savings: $624,000")
        print("  vs Traditional Maintenance: 89% cost reduction")
        print()
        print("  AI Model Performance:")
        print("    • Prediction Accuracy: 87%")
        print("    • Average Lead Time: 45 days")
        print("    • False Positives: 8%")
        print("    • API Response Time: 342ms avg")
    
    def run_demo(self):
        self.print_header()
        
        print("  Starting AeroPredict demonstration...")
        time.sleep(1)
        
        self.show_fleet_status()
        time.sleep(2)
        
        self.show_engine_monitoring()
        time.sleep(2)
        
        print("\n  🚨 CRITICAL ALERT: Engine #2 showing high failure probability!\n")
        time.sleep(2)
        
        self.simulate_sensor_data(2)
        time.sleep(2)
        
        self.predict_failure(2)
        time.sleep(2)
        
        self.automate_response()
        time.sleep(2)
        
        self.show_cost_comparison()
        time.sleep(2)
        
        self.show_monthly_impact()
        
        print("\n" + "="*80)
        print("  ✅ DEMO COMPLETE - AeroPredict Successfully Prevented a $52K Failure")
        print("="*80 + "\n")
        
        print("  Key Takeaways:")
        print("    ✓ AI predicted failure 15 days in advance")
        print("    ✓ Parts automatically ordered (saved $8,400 vs rush)")
        print("    ✓ Maintenance scheduled with zero flight impact")
        print("    ✓ Total savings: $45,500 (89% cost reduction)")
        print("    ✓ Fully automated - no human intervention required")
        print()

if __name__ == "__main__":
    demo = AeroPredictDemo()
    demo.run_demo()
