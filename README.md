# JetCore
Programming core with utilities and features

Whats this?
=
JetCore - Lightweight kernel for python programming.
This core easy to use and takes up almost no space.

Features
=
-Fast threading:

    import JetCore
    JetCore.thread(target, count)
    #target - Assing executable function/class
    #count - Count of threands be used
    
-Easy site available check:

    import JetCore
    JetCore.check_site(site)
    #site - URL of checking site

-Easy ping check:

    import JetCore
    JetCore.check_ping(ip)
    #ip - IP or URL of site/machine

-Easy External IP check:
    
    import JetCore
    JetCore.get_ip()
    #get_ip - Getting external IP of your machine
    
-Encoding str to bytes:

    import JetCore
    JetCore.str_byte(text)
    #text - str nedeed to encode
  
  
-Converting bytes to str:

    import JetCore
    JetCore.byte_str(text)
    #text - bytes nedeed to decode

-Find out the name of OS:

    import JetCore
    JetCore.platform()
    #JetCore.platform - returning name of OS
    
-Find out info of processor:

    import JetCore
    JetCore.processor()
    #JetCore.processor - returning name of processor in machine

-Find out architecture:

    import JetCore
    JetCore.arch()
    #JetCore.arch - returning architecture of processor

-Find out installed python version:

    import JetCore
    JetCore.py_ver()
    #JetCore.py_ver - returning version of installed python

-Find out info of your machine:

    import JetCore
    JetCore.machine_info()
    #JetCore.machine_info - returning info of machine: arch, system name, processor, version of installed python

How to install?
=
1) git clone https://github.com/Jetstrike-AI/JetCore
2) Copy to Libs of your python
3) Done!
