# openai function calling to create bar graph based on mockup nvidia stockprice data
# จะรันได้ต้องมี openai api key ใน PATH (windows), terminal environment (mac/linux)
# spreadsheet_path hardcode เป็นชื่อ file MOCK_NVIDIA_ONEDAY.xlsx, sheet name ต้องใช้ excel แก้ชื่อ sheet จาก ชื่อเดิมเป็น MOCK_NVIDIA_ONEDAY
# ***  IN DEVELOPEMENT CODE DO NOT USE IN PRODUCTION ***
from openai import OpenAI
import pandas as pd
import matplotlib.pyplot as plt

client = OpenAI()

def create_charts_from_spreadsheet(spreadsheet_path, sheet_name=None):
    # Read the spreadsheet
    if sheet_name:
        df = pd.read_excel(spreadsheet_path, sheet_name=sheet_name)
    else:
        df = pd.read_excel(spreadsheet_path)
    
    # Assuming the spreadsheet has two columns: 'Time' and 'Stock Price'
    time = df['Time']
    stock_price = df['stock_price_nvidia']
    
    # Create a bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(time, stock_price, color='skyblue')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.title('Stock Price at Different Times')
    bar_graph_path = 'bar_graph.png'
    plt.savefig(bar_graph_path)
    plt.close()
    
    return bar_graph_path

assistant = client.beta.assistants.create(
    instructions="You are a data visualization assistant. Use the provided functions to create charts from spreadsheet data.",
    model="gpt-4o",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "create_charts_from_spreadsheet",
                "description": "Create a bar graph from stock price data on time between 9.00am - 12.00 am and 13.00 -16.00 and save them as PNG images and output them as image url.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spreadsheet_path": {
                            "type": "string",
                            "description": "The file path to the spreadsheet."
                        },
                        "sheet_name": {
                            "type": "string",
                            "description": "The name of the sheet to read from (optional)."
                        }
                    },
                    "required": ["spreadsheet_path"]
                }
            }
        }
            ]
        )

# Example usage
spreadsheet_path = 'MOCK_NVIDIA_ONEDAY.xlsx'
sheet_name = 'MOCK_NVIDIA_ONEDAY'
create_charts_from_spreadsheet(spreadsheet_path, sheet_name)
