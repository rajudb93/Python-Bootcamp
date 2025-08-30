import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# --- Sample Data Generation ---
# In a real-world scenario, you would load this data from a CSV, database, or API.
def generate_sample_data(num_records=100):
    """Generates a Pandas DataFrame with sample production incident data."""
    np.random.seed(42)  # for reproducibility
    priorities = ['P1', 'P2', 'P3', 'P4']
    root_causes = ['Code Defect', 'Infrastructure', 'Database', 'Configuration', 'External Service']
    applications = ['Auth Service', 'Payment Gateway', 'User Profile API', 'Data Processor', 'Frontend App']
    
    # Generate dates for the last 8 weeks
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=8)
    dates = [start_date + timedelta(seconds=np.random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(num_records)]
    
    data = {
        'incident_id': range(1, num_records + 1),
        'priority': np.random.choice(priorities, num_records, p=[0.1, 0.3, 0.4, 0.2]),
        'root_cause': np.random.choice(root_causes, num_records, p=[0.4, 0.2, 0.15, 0.15, 0.1]),
        'application': np.random.choice(applications, num_records),
        'created_date': dates
    }
    return pd.DataFrame(data)

# --- Data Processing ---
df = generate_sample_data(200)

# Ensure 'created_date' is a datetime object
df['created_date'] = pd.to_datetime(df['created_date'])

# Extract week for trend analysis
df['week'] = df['created_date'].dt.isocalendar().week

# --- Plotting Functions (Modified to plot on a given subplot axis) ---

def plot_incidents_by_priority(ax, df):
    """Creates a bar chart of incident counts by priority on a given axis."""
    priority_counts = df['priority'].value_counts().sort_index()
    bars = ax.bar(priority_counts.index, priority_counts.values, color=['#FF6B6B', '#FFD166', '#06D6A0', '#118AB2'])
    
    ax.set_title('Production Incidents by Priority', fontsize=16, fontweight='bold')
    ax.set_xlabel('Priority Level', fontsize=12)
    ax.set_ylabel('Number of Incidents', fontsize=12)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add data labels
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, int(yval), ha='center', va='bottom')

def plot_incidents_by_root_cause(ax, df):
    """Creates a pie chart of incident distribution by root cause on a given axis."""
    cause_counts = df['root_cause'].value_counts()
    
    # Explode the largest slice
    explode = [0.1 if i == 0 else 0 for i in range(len(cause_counts))]
    
    ax.pie(cause_counts, labels=cause_counts.index, autopct='%1.1f%%', startangle=140,
            wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12}, explode=explode,
            colors=plt.cm.Paired.colors)
    
    ax.set_title('Incident Distribution by Root Cause', fontsize=16, fontweight='bold')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

def plot_incidents_by_application(ax, df):
    """Creates a horizontal bar chart of incident counts by application on a given axis."""
    app_counts = df['application'].value_counts().sort_values(ascending=True)
    
    bars = ax.barh(app_counts.index, app_counts.values, color=plt.cm.viridis(np.linspace(0, 1, len(app_counts))))
    
    ax.set_title('Production Incidents by Application', fontsize=16, fontweight='bold')
    ax.set_xlabel('Number of Incidents', fontsize=12)
    ax.set_ylabel('Application Name', fontsize=12)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    
    # Add data labels
    for index, value in enumerate(app_counts):
        ax.text(value + 0.5, index, str(value), va='center')

def plot_weekly_incident_trend(ax, df):
    """Creates a line chart showing the weekly trend of incidents on a given axis."""
    weekly_counts = df.groupby('week').size().sort_index()

    ax.plot(weekly_counts.index, weekly_counts.values, marker='o', linestyle='-', color='#3A86FF', markersize=8, linewidth=2)
    
    ax.set_title('Weekly Incident Trend', fontsize=16, fontweight='bold')
    ax.set_xlabel('Week Number', fontsize=12)
    ax.set_ylabel('Number of Incidents', fontsize=12)
    ax.set_xticks(weekly_counts.index)
    ax.tick_params(axis='x', rotation=45)
    ax.set_yticks(np.arange(0, weekly_counts.max() + 5, 5))
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Add data labels
    for week, count in weekly_counts.items():
        ax.text(week, count + 0.5, str(count), ha='center')

# --- Main Execution ---
if __name__ == "__main__":
    print("Generating incident report dashboard...")
    
    # Create a single figure with a 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('Production Incident Dashboard', fontsize=24, fontweight='bold')

    # Plot each graph on its respective axis
    plot_incidents_by_priority(axes[0, 0], df)
    plot_incidents_by_root_cause(axes[0, 1], df)
    plot_incidents_by_application(axes[1, 0], df)
    plot_weekly_incident_trend(axes[1, 1], df)
    
    # Adjust layout to prevent overlap and save the figure
    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    plt.savefig('incident_dashboard.png')
    plt.close()
    
    print("\nDashboard has been generated and saved as incident_dashboard.png")