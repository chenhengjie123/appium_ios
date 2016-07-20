//
//  WebViewController.m
//  appForUITest
//
//  Created by hengjie chen on 18/7/2016.
//  Copyright © 2016 hengjie chen. All rights reserved.
//

#import "WebViewController.h"

@interface WebViewController () <UIWebViewDelegate>

@end

@implementation WebViewController

- (void)viewDidLoad {
    // 进入后自动加载默认界面内容
    [super viewDidLoad];
    [self.webView loadHTMLString:@"This is test page. <br /> <a href='iostest://test'>点击后 testLabel 变成 abc</a>" baseURL:[NSURL URLWithString:@"http://baidu.com"]];
    self.webView.delegate = self;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (IBAction)goToUrl:(UIButton *)sender {
    // 点击 Go 按钮后，触发 WebView 加载对应网站内容
    NSString *fullURL = [self.urlTextField text];
    NSURL *url = [NSURL URLWithString:fullURL];
    NSURLRequest *requestObj = [NSURLRequest requestWithURL:url];
    [self.webView loadRequest:requestObj];
}

#pragma mark - UIWebViewDelegate

- (BOOL)webView:(UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType
{
    NSURL *url = [request URL];
    if([[url scheme] isEqualToString:@"iostest"]) {
        // 请求的网址是 iostest:// 开头，自动修改原生界面内容
        [self.testLabel setText:@"abc"];
        // 在 WebView 中执行 javascript 代码，弹出弹窗
        [self.webView stringByEvaluatingJavaScriptFromString:@"alert('成功把 testLabel 设置成 abc !')"];
    }
    return YES;
}

- (void)webViewDidStartLoad:(UIWebView *)webView{
    
}

- (void)webViewDidFinishLoad:(UIWebView *)webView{
    
}

- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error{
    
}



/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
