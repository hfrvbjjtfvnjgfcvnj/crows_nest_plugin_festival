import os

class NotifierFunctor:
  def __init__(self,config):
    pass
  
  def __call__(self,config,title,msg_text,priority,sound,url):
    festival_notifier_alert_on=config.get("festival_notifier_alert_on",[]);
    if ("*" in festival_notifier_alert_on) or (sound in festival_notifier_alert_on):
        cmd="%s/festival_notifier/falert.sh '%s' '%s' '%d' '%s' '%s' " %(config['plugin_path'],title,msg_text,priority,sound,url);
        os.system(cmd);
    

