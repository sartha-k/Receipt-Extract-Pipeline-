import easyocr
import re
import cv2
from task3a import preprocess_receipt
def extract_info(image_path):
    processed_img = preprocess_receipt(image_path)
    reader = easyocr.Reader(['en'], gpu=False) 
    results = reader.readtext(processed_img)
    
    data = {
        "store_name": {"value": "Unknown", "confidence": 0},
        "date": {"value": None, "confidence": 0},
        "total_amount": {"value": None, "confidence": 0}
    }

    if not results:
        return data

    # 1. Store Name
    data["store_name"]["value"] = results[0][1]
    data["store_name"]["confidence"] = float(results[0][2])
  
    all_prices = []
    for i, (bbox, text, prob) in enumerate(results):
        clean_text = text.upper().strip().replace(' ', '')
        
        # 2. Date Search
        date_match = re.search(r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})', clean_text)
        if date_match and not data["date"]["value"]:
            data["date"]["value"] = date_match.group()
            data["date"]["confidence"] = float(prob)

        # 3. Price Search with Filter
        price_match = re.search(r'(\d+\.\d{2})', clean_text)
        if price_match:
            price_val = float(price_match.group())
            
            # FILTER: Only consider numbers under 5000 as potential prices
            if price_val < 5000:
                if any(k in clean_text for k in ["TOTAL", "AMT", "DUE", "SUM"]):
                    data["total_amount"]["value"] = str(price_val)
                    data["total_amount"]["confidence"] = float(prob)
                else:
                    all_prices.append((price_val, float(prob)))

    # 4. Fallback: Largest realistic price found
    if not data["total_amount"]["value"] and all_prices:
        largest_price = max(all_prices, key=lambda x: x[0])
        data["total_amount"]["value"] = str(largest_price[0])
        data["total_amount"]["confidence"] = largest_price[1]

    return data


if __name__ == "__main__":

    image_to_test = '0.jpg' 
    print(f"--- Processing {image_to_test} ---")
    
    try:
        result_data = extract_info(image_to_test)
        print("\nExtracted Data:")
        print(result_data)
    except Exception as e:
        print(f"An error occurred: {e}")
