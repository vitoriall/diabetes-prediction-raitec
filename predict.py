import joblib
import pandas as pd

def main():
    model_path = "models/final_model.pkl"
    model = joblib.load(model_path)
    
    print("Teste de previsão do modelo Diabetes (digite 'sair' para encerrar)")
    colunas = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    
    while True:
        entrada = input(f"Digite os valores separados por vírgula ({', '.join(colunas)}): ")
        if entrada.lower() == 'sair':
            break
        
        try:
            valores = [float(x.strip()) for x in entrada.split(',')]
            if len(valores) != len(colunas):
                print(f"Erro: Você deve digitar exatamente {len(colunas)} valores.")
                continue
            
            # Cria DataFrame com colunas nomeadas para o modelo
            entrada_df = pd.DataFrame([valores], columns=colunas)
            
            prob = model.predict_proba(entrada_df)[0][1]
            pred = model.predict(entrada_df)[0]
            
            if pred == 1:
                print(f"Resultado: Paciente provavelmente TEM diabetes. (Probabilidade: {prob*100:.1f}%)")
            else:
                print(f"Resultado: Paciente provavelmente NÃO tem diabetes. (Probabilidade: {(1 - prob)*100:.1f}%)")
                
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números separados por vírgula.")

if __name__ == "__main__":
    main()
