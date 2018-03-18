package com.serverless;

import java.util.Map;
import java.io.IOException;
import java.net.URI;
import org.apache.log4j.Logger;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Handler implements RequestHandler<Map<String, Object>, String> {

	private static final Logger LOG = Logger.getLogger(Handler.class);
	private static final String BASE_URL = "https://ja.wikipedia.org/wiki/";
	//private TwitterApi twitterApi;

	@Override
	public String handleRequest(Map<String, Object> input, Context context) {
		LOG.info("received: " + input);
		try {
			//twitterApi.tweet("test");
			System.out.println(System.getenv("variable1"));
			return getContent("Template:今日は何の日");
		} catch (Exception e) {
			return "error";
		}
	}

	public String getContent(String keyword) throws Exception {
		String xml = "";
		String url = getUrl(keyword);

		Document document = getDocumentFromFrom(url);
		Elements elements = document.select("#mw-content-text ul");

		for (Element element : elements) {
			Elements lis = element.select("li");
			for (Element li : lis) {
				xml += elementToWord(li);
			}
		}

		return xml;
	}

	private String elementToWord(Element element) {
		String str = "";

		str += "◆";
		str += element.text();
		str += "\n";

		return str;
	}

	private static Document getDocumentFromFrom(String requestUrl)
			throws IOException {
		Document document = Jsoup.connect(requestUrl).get();
		return document;
	}

	private static String getUrl(String keyword) throws Exception {
		return new URI(BASE_URL + keyword).toASCIIString();
	}
}