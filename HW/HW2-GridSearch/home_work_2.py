import numpy as np
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from itertools import product
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

results = {}
best_model = None
best_model_params = None
file_writer = None


# Core function to run the model to fit and predict the results.
def run(a_clf, data, clf_hyper={}):
    M, L, n_folds = data  # unpack data container
    kf = KFold(n_splits=n_folds)  # Establish the cross validation
    ret = {}  # classic explication of results

    for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
        clf = a_clf(**clf_hyper)  # unpack parameters into clf is they exist
        clf.fit(M[train_index], L[train_index])
        pred = clf.predict(M[test_index])
        ret[ids] = {'clf': clf, 'accuracy': accuracy_score(L[test_index], pred)}
    return ret


# function to print the messages to sysout and save it to file.
def print_n_save(message):
    global file_writer
    print(message)
    file_writer.write(message + "\n")


# function to that runs all model and provides all the results.
def get_model_results(clf_grids, data):

    global best_model
    global best_model_params
    global results

    for name in clf_grids.keys():
        clf = clf_grids[name]['model']
        param_grid = clf_grids[name]['param_grid']
        temp_results2 = {}

        unpack_param_grid_lst = list(unpack_params(param_grid))
        for j in range(len(unpack_param_grid_lst)):
            temp_results3 = run(clf, data, clf_hyper=unpack_param_grid_lst[j])
            low_acc = 0
            for fold in temp_results3.keys():
                low_acc = low_acc + temp_results3[fold]['accuracy']
            low_acc = low_acc / len(temp_results3.keys())

            best_acc = -1
            if low_acc > best_acc:
                best_model = clf
                best_model_params = unpack_param_grid_lst[j]
                best_acc = low_acc

            temp_results2.update({j: {'params': unpack_param_grid_lst[j], 'results': temp_results3}})
        results.update({name: temp_results2})


# function to that format results for each grid parameters
def format_results_single_grid(a_clf, grid_no=0):
    param_all = []
    acc_all = []
    mean = []
    std = []

    params = results[a_clf][grid_no]['params']
    accs = []
    for fold in results[a_clf][grid_no]['results'].keys():
        acc = results[a_clf][grid_no]['results'][fold]['accuracy']
        accs.append(acc)

    mean_acc = np.mean(accs)
    std_acc = np.std(accs)

    param_all.append(params)
    acc_all.append(accs)
    mean.append(mean_acc)
    std.append(std_acc)

    return(param_all, acc_all, mean, std)


# function to visualize single grid
def visualize_single_grid(a_clf, grid_no=0, fig_size=(20, 4)):
    global file_writer
    param_all, acc_all, mean, std = format_results_single_grid(a_clf, grid_no)

    fig1, axes = plt.subplots(nrows=1, ncols=2, figsize=fig_size)

    # Box Plot
    axes[0].boxplot(acc_all)
    axes[0].set_title("Classifier Resample Scores Comparison | Classifier '{}', Grid {}".format(a_clf, grid_no))
    axes[0].set_xlabel('Classifier Number')
    axes[0].set_ylabel('Accuracy')

    # Scatter Plot
    axes[1].scatter(mean, std, alpha=0.5)
    axes[1].set_title("Bias / Variance Analysis | Classifier '{}', Grid {}".format(a_clf, grid_no))
    axes[1].set_xlabel('Mean Resample Scores per Classifier')
    axes[1].set_ylabel('Std of Resample Scores per Classifier')

    print_n_save("-" * 50)
    print_n_save("Classifier '{}', Grid {}".format(a_clf, grid_no))
    print_n_save("-" * 50)
    for index, (m, s, param) in enumerate(zip(mean, std, param_all)):
        print_n_save("Accuracy: {:>5.3f} (+/-{:>5.3f} 95% CI) | Params: {}".format(m, s * 2, param))
    print()


# function to visualize all the models.
def visualize_all_grids(fig_size=(20, 4)):

    for clf in results.keys():
        for grid_no in results[clf].keys():
            visualize_single_grid(clf, grid_no, fig_size)


def unpack_params(clf_hyper={}):
    keys, values = zip(*clf_hyper.items())
    for bundle in product(*values):
        d = dict(zip(keys, bundle))
        yield d


if __name__ == '__main__':

    # 2. Expand to include larger number of classifiers and hyperparameter settings
    clf_grids = {'LR': {'model': LogisticRegression,
                        'param_grid': {'C': [1, 10], 'max_iter': [500, 1000]}},
                 'SVM': {'model': SVC,
                         'param_grid': {'C': [0.01, 0.1, 1, 10], 'kernel': ['linear']}},
                 'RF': {'model': RandomForestClassifier,
                        'param_grid': {'n_estimators': [50, 100], 'max_features': ['auto', 'sqrt']}}}

    file_writer = open("classifier_results.txt", "w")

    # 3. Find some simple data
    iris_dataset = datasets.load_iris()
    M = np.array(iris_dataset['data'])
    L = np.array(iris_dataset['target'])
    n_folds = 5

    data = (M, L, n_folds)
    get_model_results(clf_grids, data)

    # 4. generate matplotlib plots that will assist in identifying the optimal clf and parampters settings
    visualize_all_grids()
    plt.show()

    print_n_save("The best model is :" + str(best_model))
    print_n_save("The best model params is :" + str(best_model_params))

    X_train, X_test, y_train, y_test = train_test_split(M, L, test_size=0.2)
    model = best_model(**best_model_params)
    model.fit(X_train, y_train)
    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)

    print_n_save("The best model accuracy with test dataset         : {:.3}".format(accuracy_score(pred_test, y_test)))

    # 5. Please set up your code to be run and save the results to the directory that its executed from
    file_writer.close()

    # 6. Investigate grid search function
    # GridSearchCV is a library function that is a member of sklearn’s model_selection package.
    # It helps to loop through predefined hyperparameters and fit your estimator (model) on your training set.
    # So, in the end, you can select the best parameters from the listed hyperparameters.

    grid_lr = GridSearchCV(estimator=LogisticRegression(), param_grid=clf_grids['LR']['param_grid'],
                           scoring='accuracy', cv=5, verbose=1, n_jobs=-1)
    grid_lr.fit(X_train, y_train)
    print('Gridsearch logistic regression best parameters :' + str(grid_lr.best_estimator_))

    grid_svm = GridSearchCV(estimator=SVC(), param_grid=clf_grids['SVM']['param_grid'],
                            scoring='accuracy', cv=5, verbose=1, n_jobs=-1)
    grid_svm.fit(X_train, y_train)
    print('Gridsearch support vector machine best parameters :' + str(grid_svm.best_estimator_))

    grid_rf = GridSearchCV(estimator=RandomForestClassifier(), param_grid=clf_grids['RF']['param_grid'],
                           scoring='accuracy', cv=5, verbose=1, n_jobs=-1)
    grid_rf.fit(X_train, y_train)
    print('Gridsearch random forest best parameters :' + str(grid_rf.best_estimator_))

    # When compared the results from SKlearn GridSearch to death to grid search implemented the results
    # were not matching.
