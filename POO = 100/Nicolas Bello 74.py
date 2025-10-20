import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

class PredictorDemandaLibros:
    def __init__(self):
        self.modelo = RandomForestClassifier(n_estimators=100, random_state=42)
        self.label_encoders = {}
        self.entrenado = False

    def preparar_datos(self, df):
        df_preparado = df.copy()
        columnas_categoricas = ['genero', 'autor', 'mes', 'dia_semana']
        for columna in columnas_categoricas:
            if columna in df_preparado.columns:
                le = LabelEncoder()
                df_preparado[columna] = le.fit_transform(df_preparado[columna])
                self.label_encoders[columna] = le
        return df_preparado

    def entrenar(self, datos_historicos):
        df = self.preparar_datos(datos_historicos)
        X = df.drop('demanda_alta', axis=1)
        y = df['demanda_alta']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.modelo.fit(X_train, y_train)
        precision = self.modelo.score(X_test, y_test)
        self.entrenado = True
        return {
            'precision': precision * 100,
            'muestras_entrenamiento': len(X_train),
            'muestras_prueba': len(X_test)
        }

    def predecir_demanda(self, libro_info):
        if not self.entrenado:
            return "Modelo no entrenado aún"
        df_input = pd.DataFrame([libro_info])
        for columna, encoder in self.label_encoders.items():
            if columna in df_input.columns:
                df_input[columna] = encoder.transform(df_input[columna])
        prediccion = self.modelo.predict(df_input)[0]
        probabilidad = self.modelo.predict_proba(df_input)[0]
        return {
            'demanda_alta': bool(prediccion),
            'probabilidad': max(probabilidad) * 100
        }

    def guardar_modelo(self, nombre_archivo='modelo_demanda.pkl'):
        joblib.dump({
            'modelo': self.modelo,
            'encoders': self.label_encoders
        }, nombre_archivo)
        return f"Modelo guardado en {nombre_archivo}"
