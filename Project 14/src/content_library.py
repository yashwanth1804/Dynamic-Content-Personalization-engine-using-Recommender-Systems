# Banking products and content mapped to customer segments
BANKING_CONTENT = {
    0: {  # Young segment
        'segment_name': 'Young Professionals',
        'products': [
            {'name': 'Student Savings Account', 'description': 'No fees, mobile banking'},
            {'name': 'First Credit Card', 'description': 'Build credit history safely'},
            {'name': 'Personal Loan', 'description': 'Quick approval, competitive rates'}
        ],
        'content': [
            {'title': 'Financial Basics for Beginners', 'type': 'guide'},
            {'title': 'Budgeting Apps Comparison', 'type': 'tool'},
            {'title': 'Building Your Credit Score', 'type': 'article'}
        ]
    },
    1: {  # Middle-aged segment
        'segment_name': 'Family Focused',
        'products': [
            {'name': 'Home Mortgage', 'description': 'Low rates for families'},
            {'name': 'Education Savings Plan', 'description': 'Save for childrens future'},
            {'name': 'Life Insurance', 'description': 'Protect your family'}
        ],
        'content': [
            {'title': 'Home Buying Guide', 'type': 'guide'},
            {'title': 'College Savings Calculator', 'type': 'tool'},
            {'title': 'Family Financial Planning', 'type': 'article'}
        ]
    },
    2: {  # Senior segment
        'segment_name': 'Pre-Retirement',
        'products': [
            {'name': 'Fixed Deposit', 'description': 'Guaranteed returns'},
            {'name': 'Retirement Planning', 'description': 'Secure your future'},
            {'name': 'Wealth Management', 'description': 'Professional advice'}
        ],
        'content': [
            {'title': 'Retirement Income Strategies', 'type': 'guide'},
            {'title': 'Investment Risk Calculator', 'type': 'tool'},
            {'title': 'Estate Planning Basics', 'type': 'article'}
        ]
    },
    3: {  # High-value segment
        'segment_name': 'Premium Customers',
        'products': [
            {'name': 'Premium Banking', 'description': 'Exclusive benefits'},
            {'name': 'Investment Portfolio', 'description': 'Diversified investments'},
            {'name': 'Business Loans', 'description': 'Grow your business'}
        ],
        'content': [
            {'title': 'Advanced Investment Strategies', 'type': 'guide'},
            {'title': 'Tax Optimization Tools', 'type': 'tool'},
            {'title': 'Market Analysis Reports', 'type': 'article'}
        ]
    }
}
