//
//  WebViewController.h
//  appForUITest
//
//  Created by hengjie chen on 18/7/2016.
//  Copyright © 2016 hengjie chen. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface WebViewController : UIViewController <UIWebViewDelegate>

@property (strong, nonatomic) IBOutlet UITextField *urlTextField;
@property (strong, nonatomic) IBOutlet UIWebView *webView;
@property (strong, nonatomic) IBOutlet UIButton *goButton;
@property (strong, nonatomic) IBOutlet UILabel *testLabel;
@end
