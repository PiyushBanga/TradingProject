import csv
import asyncio
import json
import pandas as pd
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings

class Candle:
    def __init__(self, id, open, high, low, close, date):
        self.id = id
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.date = date

async def process_candles(candles, timeframe):
    # convert the candles into the given timeframe
    # ...

    return converted_candles

def handle_upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        timeframe = request.POST.get('timeframe')

        # read the CSV file
        pd.options.mode.chained_assignment = None
        df = pd.read_csv(uploaded_file, low_memory=False)
        candles = []
        for index, row in df.iterrows():
            candle = Candle(row['id'], row['open'], row['high'], row['low'], row['close'], row['date'])
            candles.append(candle)

        # process the candles asynchronously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        converted_candles = loop.run_until_complete(process_candles(candles, timeframe))

        # convert the candles to JSON and write to a file
        json_data = json.dumps([candle.__dict__ for candle in converted_candles])
        filename = 'converted_candles.json'
        filepath = f'{settings.MEDIA_ROOT}/{filename}'
        with open(filepath, 'w') as f:
            f.write(json_data)

        # return the JSON file for download
        file = open(filepath, 'r')
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response

    return render(request, 'MainApp/upload.html')
