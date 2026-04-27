import os
import json
from task3bc import extract_info

def run_pipeline(input_folder, output_folder):
    # 1. Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    all_data = []
    total_spend = 0.0
    #Looping
    image_extensions = ('.jpg', '.jpeg', '.png')
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(image_extensions)]

    print(f"Found {len(files)} receipts. Starting processing...")

    for filename in files:
        img_path = os.path.join(input_folder, filename)
        print(f"Processing: {filename}...")
        try:
            #extract information from the image data
            data = extract_info(img_path)

            json_filename = os.path.splitext(filename)[0] + ".json"
            with open(os.path.join(output_folder, json_filename), 'w') as f:
                json.dump(data, f, indent=4)
            
            all_data.append(data)
               
            if data["total_amount"]["value"]:
                total_spend += float(data["total_amount"]["value"])
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    summary = {
        "total_receipts_processed": len(all_data),
        "total_expenditure": round(total_spend, 2),
        "average_spend": round(total_spend / len(all_data), 2) if all_data else 0
    }

    with open('financial_summary.json', 'w') as f:
        json.dump(summary, f, indent=4)

    print("\n--- Processing Complete ---")
    print(f"Summary: Total Spend = {summary['total_expenditure']}")
    print("Check the 'outputs' folder for individual JSON files.")

if __name__ == "__main__":
    run_pipeline(input_folder='./imgs', output_folder='./outputs')
