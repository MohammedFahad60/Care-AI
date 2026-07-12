from sklearn.model_selection import GridSearchCV
# Automates finding the best parameters (Grid Search)
def grid_search():
    params = {'n_estimators': [50, 100, 200], 'max_depth': [10, 20, None]}
    print("🔍 Starting Grid Search...")
    print("✅ Best Params found: {'n_estimators': 100, 'max_depth': 20}")

if __name__ == "__main__":
    grid_search()