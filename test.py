import cv2
from pyzbar import pyzbar
from api import fetch_product_data, extract_and_print_data

def capture_barcode(timeout=10):
    cap = cv2.VideoCapture(0)
    barcode_data = None
    start_time = cv2.getTickCount()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (barcode.rect.left, barcode.rect.top), 
                          (barcode.rect.left + barcode.rect.width, barcode.rect.top + barcode.rect.height), 
                          (0, 255, 0), 2)
            cv2.putText(frame, barcode_data, (barcode.rect.left, barcode.rect.top - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Barcode Scanner', frame)

        # Check for key press or timeout
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if barcode_data or cv2.waitKey(1) & 0xFF == ord('q') or elapsed_time > timeout:
            break

    cap.release()
    cv2.destroyAllWindows()
    return barcode_data

def main():
    barcode = capture_barcode()
    if barcode:
        print(f"Barcode: {barcode}")
        data = fetch_product_data(barcode)
        extract_and_print_data(data)
    else:
        print("No barcode detected.")

if __name__ == "__main__":
    main()
