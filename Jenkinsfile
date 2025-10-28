node {
    stage('Checkout') {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                      url: 'git@github.com:soufianta/python-web-app.git',
                      credentialsId: 'jenkins'
                  ]]
        ])
    }

    stage('Setup Python') {
        sh '''
        python3 --version
        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        '''
    }

    stage('Run App') {
        sh '''
        . venv/bin/activate
        python app.py
        '''
    }
}
