#!/usr/bin/python3

# importar el AWS SDK 
import boto3
import traceback

aws_access_key_id='AKIAXSC5CRZ4Z4QYUBGP'
aws_secret_access_key='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'

# crear el cliente de polly con sus credenciales
polly_client = boto3.Session(
    aws_access_key_id=aws_access_key_id,                  
    aws_secret_access_key=aws_secret_access_key,
    region_name='us-east-1').client('polly')

# realizar la llamada con parámetros
try:
    response = polly_client.start_speech_synthesis_task(
        VoiceId='Lucia',
        OutputFormat='mp3', 
        OutputS3BucketName='ivanlopez-riberadeltajo-bucket1',
        Text='En un lugar de la Mancha, de cuyo nombre no quiero acordarme, ' + 
             'no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, '+
             'adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca'+
             ' que carnero, salpicón las más noches, duelos y quebrantos los sábados,'+
             ' lantejas los viernes, algún palomino de añadidura los domingos, consumían'+
             ' las tres partes de su hacienda. ',
        TextType='text',
        SampleRate='22050')

    print("El fichero de audio se ha guardado en {} ".format(response['SynthesisTask']['OutputUri']))
except:
    print("excepción al conectarse a polly!")
    traceback.print_exc()
