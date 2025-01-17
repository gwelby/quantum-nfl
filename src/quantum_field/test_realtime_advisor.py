"""
Test the RealtimeQuantumAdvisor
"""

import asyncio
import logging
from realtime_quantum_advisor import RealtimeQuantumAdvisor

logging.basicConfig(level=logging.INFO)

async def main():
    # Create advisor
    advisor = RealtimeQuantumAdvisor()
    
    print("\nStarting Real-time Quantum NFL Analysis")
    print("=" * 50)
    print("\nVisualization window will open automatically.")
    print("Press Ctrl+C to stop the analysis.\n")
    
    try:
        # Start real-time analysis
        await advisor.start_realtime_analysis()
    except KeyboardInterrupt:
        print("\nStopping analysis...")
        advisor.stop()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        advisor.stop()

if __name__ == "__main__":
    asyncio.run(main())
