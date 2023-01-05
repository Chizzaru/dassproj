import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score




def randomForestAnxiety(arr):
    # Load the CSV file
    df = pd.read_csv('Final DataSet of DASS21 - Anxiety.csv')

    # Extract the features and labels from the DataFrame
    X = df.drop('SaverityLevel', axis=1)
    y = df['SaverityLevel']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create a random forest classifier
    clf = RandomForestClassifier()

    # Train the classifier using the training data
    clf.fit(X_train, y_train)


    new_sample = arr
    newSample = pd.DataFrame ([new_sample], columns = ['q2','q4','q7','q9','q15','q19','q20'])


    y_pred = clf.predict(newSample)

    return y_pred[0]

    # Compute the accuracy of the classifier
    # accuracy = accuracy_score(X_test, y_pred)

    # print(accuracy)

def randomForestDepression(arr):
    # Load the CSV file
    df = pd.read_csv('Final DataSet of DASS21 - Depression.csv')

    # Extract the features and labels from the DataFrame
    X = df.drop('SaverityLevel', axis=1)
    y = df['SaverityLevel']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create a random forest classifier
    clf = RandomForestClassifier()

    # Train the classifier using the training data
    clf.fit(X_train, y_train)


    new_sample = arr
    newSample = pd.DataFrame ([new_sample], columns = ['q3','q5','q10','q13','q16','q17','q21'])


    y_pred = clf.predict(newSample)

    return y_pred[0]

    # Compute the accuracy of the classifier
    # accuracy = accuracy_score(X_test, y_pred)

    # print(accuracy)


def randomForestStress(arr):
    # Load the CSV file
    df = pd.read_csv('Final DataSet of DASS21 - Stress.csv')

    # Extract the features and labels from the DataFrame
    X = df.drop('SaverityLevel', axis=1)
    y = df['SaverityLevel']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create a random forest classifier
    clf = RandomForestClassifier()

    # Train the classifier using the training data
    clf.fit(X_train, y_train)


    new_sample = arr
    newSample = pd.DataFrame ([new_sample], columns = ['q1','q6','q8','q11','q12','q14','q18'])


    y_pred = clf.predict(newSample)

    return y_pred[0]

    # Compute the accuracy of the classifier
    # accuracy = accuracy_score(X_test, y_pred)

    # print(accuracy)



#data = [0,0,0,0,0,0,0]
#print(randomForestAnxiety(data))