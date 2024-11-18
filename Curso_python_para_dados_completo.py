import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

class Modelo:
    def __init__(self):
        self.df = None
        self.models = None
        self.X_test = None
        self.y_test = None

    def CarregarDataset(self, path):
        """Carrega o conjunto de dados Iris."""
        names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
        self.df = pd.read_csv(path, names=names)
        print("Dataset carregado com sucesso.")

    def TratamentoDeDados(self):
        """Realiza o pré-processamento dos dados."""
        # Codifica as classes (espécies de flores) em valores numéricos
        self.df['Species'] = self.df['Species'].astype('category').cat.codes
        print("Dados pré-processados com sucesso.")

    def Treinamento(self):
        """Treina os modelos SVM e Regressão Logística."""
        # Divide os dados em conjuntos de treino e teste
        X = self.df.drop('Species', axis=1)
        y = self.df['Species']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Treinamento dos modelos
        svm_model = SVC(kernel='linear', random_state=42)
        lr_model = LogisticRegression(max_iter=200, random_state=42)

        svm_model.fit(X_train, y_train)
        lr_model.fit(X_train, y_train)

        self.models = {'SVM': svm_model, 'Logistic Regression': lr_model}
        self.X_test = X_test
        self.y_test = y_test
        print("Modelos treinados com sucesso.")

    def Teste(self):
        """Avalia o desempenho dos modelos nos dados de teste."""
        results = {}
        for model_name, model in self.models.items():
            y_pred = model.predict(self.X_test)
            acc = accuracy_score(self.y_test, y_pred)
            cm = confusion_matrix(self.y_test, y_pred)
            report = classification_report(self.y_test, y_pred, output_dict=True)

            results[model_name] = {
                'accuracy': acc,
                'confusion_matrix': cm,
                'classification_report': report
            }

            # Exibe os resultados
            print(f"\nModelo: {model_name}")
            print(f"Acurácia: {acc:.2f}")
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                        xticklabels=['Setosa', 'Versicolor', 'Virginica'],
                        yticklabels=['Setosa', 'Versicolor', 'Virginica'])
            plt.title(f"Matriz de Confusão - {model_name}")
            plt.xlabel("Predito")
            plt.ylabel("Real")
            plt.show()

        return results

    def Train(self):
        """Executa o fluxo completo do treinamento."""
        self.CarregarDataset("C:/Users/usuario/Downloads/iris.data")
        self.TratamentoDeDados()
        self.Treinamento()
        return self.Teste()

# Instancia e executa o modelo
if __name__ == "__main__":
    modelo = Modelo()
    modelo.Train()
