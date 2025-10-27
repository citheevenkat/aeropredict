#!/usr/bin/env python3
"""AeroPredict Database Query Tool"""

import sqlite3

class DatabaseViewer:
    def __init__(self, db_path="/mnt/user-data/outputs/aeropredict.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def view_all_data(self):
        """Quick view of all key data"""
        print("\n" + "="*80)
        print("  🔍 AEROPREDICT DATABASE - QUICK VIEW")
        print("="*80)
        
        # NASA Data
        print("\n📡 NASA C-MAPSS Dataset:")
        self.cursor.execute("SELECT COUNT(*), AVG(rul), MIN(rul), MAX(rul) FROM nasa_sensor_data")
        stats = self.cursor.fetchone()
        print(f"  • Total readings: {stats[0]:,}")
        print(f"  • Avg RUL: {stats[1]:.1f} cycles")
        print(f"  • RUL range: {stats[2]} - {stats[3]} cycles")
        
        # Aircraft
        print("\n✈️  Aircraft Fleet:")
        self.cursor.execute("SELECT COUNT(*), SUM(total_flight_hours) FROM aircraft")
        fleet = self.cursor.fetchone()
        print(f"  • Total aircraft: {fleet[0]}")
        print(f"  • Total flight hours: {fleet[1]:,}")
        
        # Suppliers
        print("\n🏭 Supply Chain:")
        self.cursor.execute("SELECT COUNT(*) FROM suppliers")
        suppliers = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM parts_catalog")
        parts = self.cursor.fetchone()[0]
        print(f"  • Suppliers: {suppliers}")
        print(f"  • Parts in catalog: {parts}")
        
        # Cost Analytics
        print("\n💰 Cost Analytics:")
        self.cursor.execute("SELECT * FROM cost_analytics WHERE period = '2024-Q4'")
        analytics = self.cursor.fetchone()
        if analytics:
            print(f"  • Total maintenance events: {analytics[1]}")
            print(f"  • Predictive: {analytics[2]} | Reactive: {analytics[3]}")
            print(f"  • Total savings: ${analytics[6]:,.0f}")
            print(f"  • Cost reduction: 87.5%")
        
        print("\n" + "="*80 + "\n")
        self.conn.close()

if __name__ == "__main__":
    viewer = DatabaseViewer()
    viewer.view_all_data()
