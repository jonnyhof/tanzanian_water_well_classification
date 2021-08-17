import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.metrics import accuracy_score, plot_confusion_matrix, f1_score, precision_score, recall_score

def metrics_matrix(classifier, x_train, y_train, x_test, y_test):
        """
        Takes a trained classifier and outputs the desired scoring metrics and a confusion matrix for the test set.
    
                Parameters: classifier (Sklearn object or Pipeline): An Sklearn classifier model that has alrady been fit to the data
                            x_train (DataFrame): The training values
                            y_train (DataFrame): The training answers
                            x_test (DataFrame): The testing values
                            y_test (DataFrame): The testing answers
                            
                Returns: A printed report of Training and testing accuracy, F1 score, precision, recall, and confusion matrix
        """
        # First predict and store training and testing values on the classifier
        train_preds = classifier.predict(x_train)
        test_preds = classifier.predict(x_test)
        
        # Compute accuracy scores
        train_acc = accuracy_score(y_train, train_preds)
        test_acc = accuracy_score(y_test, test_preds)
        
        # Compute F1 scores, average = weighted for multiclass
        train_f1 = f1_score(y_train, train_preds, average='weighted')
        test_f1 = f1_score(y_test, test_preds, average='weighted')
        
        # compute precision
        train_pre = precision_score(y_train, train_preds, average='weighted')
        test_pre = precision_score(y_test, test_preds, average='weighted')
        
        # Compute recall
        train_rec = recall_score(y_train, train_preds, average='weighted')
        test_rec = recall_score(y_test, test_preds, average='weighted')
        
        
        # Print the results
        print("\033[1m" + 'Train Scores:' + "\033[0m")
        print(
        f"""       Accurary = {train_acc:.2}   F1 Score = {train_f1:.2}
        Precision = {train_pre:.2}   Recall = {train_rec:.2}
        
        ----------------
        """)
        print("\033[1m" + 'Test Scores:' + "\033[0m")
        print(
        f"""       Accurary = {test_acc:.2}   F1 Score = {test_f1:.2}
        Precision = {test_pre:.2}   Recall = {test_rec:.2}
        """)
        
        # Plot the confusion matrix for the testing set
        plot_confusion_matrix(classifier, x_test, y_test, xticks_rotation=30)
        plt.title('Testing Set Confusion Matrix')
        plt.show(); 