pipeline {
    agent {
        docker {
            image 'python:3.8.10'
            args '-u root:root' // Run as root if needed for pip installs
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning GitHub repository...'
                git 'https://github.com/prasadkkl/python_sel_pyt_po.git'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Executing run_tests.sh...'
                sh './run_tests.sh'
            }
        }

        stage('Archive Reports') {
            steps {
                echo 'Archiving test reports...'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }

        success {
            echo 'Tests passed successfully.'
        }

        failure {
            echo 'Tests failed.'
        }
    }
}
