package com.serverless;

import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;

public class TwitterApi {
	private final Twitter twitter;

	public TwitterApi() {
		twitter = new TwitterFactory().getInstance();
	}

	public void tweet(String content) throws TwitterException {
		twitter.updateStatus(content);
	}
}