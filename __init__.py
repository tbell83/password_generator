from flask import Flask
from flask import render_template, request
import passwd_gen
import github_verify
import code_deploy

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def get_pass():
        return passwd_gen.generate_password()
    return dict(get_pass=get_pass)


@app.route('/')
def root():
    return render_template('password.html')


@app.route('/deploy', methods=['POST'])
def deploy():
    data = request.data
    signature = request.headers.get('X-Hub-Signature')
    if github_verify.verifyHmacHash(data, signature):
        code_deploy.deploy()
        return 'Successful Deployment'
    else:
        return 'No Vas'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
