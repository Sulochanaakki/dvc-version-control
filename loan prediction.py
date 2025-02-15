{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ed22c71c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ff8c5bcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0         NaN             360.0   \n",
       "1             4583             1508.0       128.0             360.0   \n",
       "2             3000                0.0        66.0             360.0   \n",
       "3             2583             2358.0       120.0             360.0   \n",
       "4             6000                0.0       141.0             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  \n",
       "0             1.0         Urban           Y  \n",
       "1             1.0         Rural           N  \n",
       "2             1.0         Urban           Y  \n",
       "3             1.0         Urban           Y  \n",
       "4             1.0         Urban           Y  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train = pd.read_csv('data/train_ctrUa4K.csv') \n",
    "train.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8073d4e7",
   "metadata": {},
   "source": [
    "We know that machine learning models take only numbers as inputs and can not process strings. So, we have to deal with the categories present in the dataset and convert them into numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2b3082c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "train['Gender']= train['Gender'].map({'Male':0, 'Female':1})\n",
    "train['Married']= train['Married'].map({'No':0, 'Yes':1})\n",
    "train['Loan_Status']= train['Loan_Status'].map({'N':0, 'Y':1})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d857d50d",
   "metadata": {},
   "source": [
    "Here, we have converted the categories present in the Gender, Married and the Loan Status variable into numbers, simply using the map function of python. Next, let’s check if there are any missing values in the dataset:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "99e6c374",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender               13\n",
       "Married               3\n",
       "Dependents           15\n",
       "Education             0\n",
       "Self_Employed        32\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount           22\n",
       "Loan_Amount_Term     14\n",
       "Credit_History       50\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "811ed06a",
   "metadata": {},
   "source": [
    "So, there are missing values on many variables including the Gender, Married, LoanAmount variable. Next, we will remove all the rows which contain any missing values in them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ac8955a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID              0\n",
       "Gender               0\n",
       "Married              0\n",
       "Dependents           0\n",
       "Education            0\n",
       "Self_Employed        0\n",
       "ApplicantIncome      0\n",
       "CoapplicantIncome    0\n",
       "LoanAmount           0\n",
       "Loan_Amount_Term     0\n",
       "Credit_History       0\n",
       "Property_Area        0\n",
       "Loan_Status          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train = train.dropna()\n",
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e65c14b0",
   "metadata": {},
   "source": [
    "Now there are no missing values in the dataset. Next, we will separate the dependent (Loan_Status) and the independent variables:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "af983cdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((480, 5), (480,))"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = train[['Gender', 'Married', 'ApplicantIncome', 'LoanAmount', 'Credit_History']]\n",
    "y = train.Loan_Status\n",
    "X.shape, y.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f54db682",
   "metadata": {},
   "source": [
    "For this particular project, I have only picked 5 variables that I think are most relevant. These are the Gender, Marital Status, ApplicantIncome, LoanAmount, and Credit_History and stored them in variable X. Target variable is stored in another variable y. And there are 480 observations available. Next, let’s move on to the model building stage.\n",
    "\n",
    "Here, we will first split our dataset into a training and validation set, so that we can train the model on the training set and evaluate its performance on the validation set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6226a51f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train, x_cv, y_train, y_cv = train_test_split(X,y, test_size = 0.2, random_state = 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16ed99c9",
   "metadata": {},
   "source": [
    "Next, we will train the random forest model using the training set:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "02916529",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(max_depth=4, random_state=10)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier \n",
    "model = RandomForestClassifier(max_depth=4, random_state = 10) \n",
    "model.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0363bb4",
   "metadata": {},
   "source": [
    "Let’s check its performance on both the training and validation set:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ef5c1c81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8020833333333334"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "pred_cv = model.predict(x_cv)\n",
    "accuracy_score(y_cv,pred_cv)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "764d076c",
   "metadata": {},
   "source": [
    "The model is 80% accurate on the validation set. Let’s check the performance on the training set too:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ff8c89e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8203125"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred_train = model.predict(x_train)\n",
    "accuracy_score(y_train,pred_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef829dd9",
   "metadata": {},
   "source": [
    "Performance on the training set is almost similar to that on the validation set. So, the model has generalized well. Finally, we will save this trained model so that it can be used in the future to make predictions on new observations:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c63f9fae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# saving the model \n",
    "import pickle \n",
    "pickle_out = open(\"classifier.pkl\", mode = \"wb\") \n",
    "pickle.dump(model, pickle_out) \n",
    "pickle_out.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3c60b12",
   "metadata": {},
   "source": [
    "We are saving the model in pickle format and storing it as classifier.pkl. This will store the trained model and we will use this while deploying the model."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e1dc09d",
   "metadata": {},
   "source": [
    "Here are some of the key features of Streamlit which I found really interesting and useful:\n",
    "\n",
    "- It quickly turns data scripts into shareable web applications. You just have to pass a running script to the tool and it can convert that to a web app.\n",
    "- Everything in Python. The best thing about Streamlit is that everything we do is in Python. Starting from loading the model to creating the frontend, all can be done using Python.\n",
    "- All for free. It is open source and hence no cost is involved. You can deploy your apps without paying for them.\n",
    "- No front-end experience required. Model deployment generally contains two parts, frontend, and backend. The backend is generally a working model, a machine learning model in our case, which is built-in python. And the front end part, which generally requires some knowledge of other languages like java scripts, etc. Using Streamlit, we can create this front end in Python itself. So, we need not learn any other programming languages or web development techniques. Understanding Python is enough.\n",
    "\n",
    "Now, let’s look at the deployment pipeline if we use Streamlit:\n",
    "\n",
    "- Model Building\n",
    "- Creating a python script\n",
    "- Create front-end: Python\n",
    "- Deploy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "afdd0840",
   "metadata": {},
   "source": [
    "### Model Deployment of the Loan Prediction model using Streamlit"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a438b510",
   "metadata": {},
   "source": [
    "!pip install -q pyngrok\n",
    "\n",
    "!pip install -q streamlit\n",
    "\n",
    "!pip install -q streamlit_ace\n",
    "\n",
    " pyngrok is a python wrapper for ngrok which helps to open secure tunnels from public URLs to localhost. This will help us to host our web app. Streamlit will be used to make our web app. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7f950c7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pip in c:\\users\\user\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (21.3.1)Note: you may need to restart the kernel to use updated packages.\n",
      "Collecting pip\n",
      "  Downloading pip-22.0.3-py3-none-any.whl (2.1 MB)\n",
      "Installing collected packages: pip\n",
      "  Attempting uninstall: pip\n",
      "\n",
      "    Found existing installation: pip 21.3.1\n",
      "    Uninstalling pip-21.3.1:\n",
      "      Successfully uninstalled pip-21.3.1\n",
      "Successfully installed pip-22.0.3\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cb6d628",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
