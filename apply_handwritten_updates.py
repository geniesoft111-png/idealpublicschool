import os, re

BASE_DIR = '/Users/silver/geniesoft/idealpublicschool'
os.chdir(BASE_DIR)

all_pages = [
    'index.html', 'about.html', 'course.html', 'course-details.html',
    'admissions.html', 'facilities.html', 'teacher.html', 'teacher-details.html',
    'student-life.html', 'gallery.html', 'books.html', 'event.html',
    'event-details.html', 'blog.html', 'blog-details.html', 'contact.html'
]

# ----------------------------------------------------
# 1. UPDATE ABOUT.HTML
# ----------------------------------------------------
print("--- 1. Updating about.html ---")
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Replace leadership cards
old_about_teachers_pattern = re.compile(
    r'<div class="row">\s*<div class="col-12">\s*<div class="section-title text-center">\s*<img src="img/icon/section\.png" alt="title-icon">\s*<h2>OUR LEADERSHIP &amp; EDUCATORS</h2>\s*</div>\s*</div>\s*</div>\s*<div class="row">.*?<!-- Teacher End -->',
    re.DOTALL
)

new_about_teachers = '''<div class="row">
                    <div class="col-12">
                        <div class="section-title text-center">
                            <img src="img/icon/section.png" alt="title-icon">
                            <h2>OUR LEADERSHIP &amp; EDUCATORS</h2>
                            <p>Visionary leadership and dedicated teachers guiding students towards academic and ethical excellence.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <!-- Leader 1: Arshi Kabir (Founder) -->
                    <div class="col-lg-3 col-md-6">
                        <div class="single-teacher">
                            <div class="single-teacher-img">
                                <a href="teacher-details.html"><img src="img/teacher/teacher1.jpg" alt="Founder &amp; Director Arshi Kabir"></a>  
                            </div>
                            <div class="single-teacher-content text-center">
                                <h2><a href="teacher-details.html">Arshi Kabir</a></h2>
                                <h4>Founder &amp; Director</h4>
                                <ul>
                                    <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                                    <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                                    <li><a href="mailto:idealschool4938@gmail.com"><i class="fa fa-envelope"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Leader 2: Rumi Kabir (Management & Administration) -->
                    <div class="col-lg-3 col-md-6">
                        <div class="single-teacher">
                            <div class="single-teacher-img">
                                <a href="about.html"><img src="img/teacher/rumi-kabir.jpg" alt="Rumi Kabir"></a>  
                            </div>
                            <div class="single-teacher-content text-center">
                                <h2><a href="about.html">Rumi Kabir</a></h2>
                                <h4>Management &amp; Administration</h4>
                                <ul>
                                    <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                                    <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                                    <li><a href="mailto:idealschool4938@gmail.com"><i class="fa fa-envelope"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Leader 3: Homa Parveen (Principal) -->
                    <div class="col-lg-3 col-md-6">
                        <div class="single-teacher">
                            <div class="single-teacher-img">
                                <a href="teacher.html"><img src="img/teacher/teacher3.jpg" alt="Principal Homa Parveen"></a>  
                            </div>
                            <div class="single-teacher-content text-center">
                                <h2><a href="teacher.html">Homa Parveen</a></h2>
                                <h4>Principal (M.A., B.Ed.)</h4>
                                <ul>
                                    <li><a href="#"><i class="fa fa-book"></i></a></li>
                                    <li><a href="#"><i class="fa fa-graduation-cap"></i></a></li>
                                    <li><a href="mailto:idealschool4938@gmail.com"><i class="fa fa-envelope"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Leader 4: Amarjeet Kumar (Senior Faculty) -->
                    <div class="col-lg-3 col-md-6">
                        <div class="single-teacher">
                            <div class="single-teacher-img">
                                <a href="teacher.html"><img src="img/teacher/teacher10.jpg" alt="Amarjeet Kumar"></a>  
                            </div>
                            <div class="single-teacher-content text-center">
                                <h2><a href="teacher.html">Amarjeet Kumar</a></h2>
                                <h4>Senior Faculty (B.A., B.Ed.)</h4>
                                <ul>
                                    <li><a href="#"><i class="fa fa-book"></i></a></li>
                                    <li><a href="#"><i class="fa fa-graduation-cap"></i></a></li>
                                    <li><a href="teacher.html"><i class="fa fa-users"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Teacher End -->'''

if old_about_teachers_pattern.search(about_content):
    about_content = old_about_teachers_pattern.sub(new_about_teachers, about_content)
    print("Updated leadership cards in about.html")
else:
    print("WARNING: Could not find leadership cards pattern in about.html")

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)


# ----------------------------------------------------
# 2. UPDATE TEACHER.HTML
# ----------------------------------------------------
print("--- 2. Updating teacher.html ---")
with open('teacher.html', 'r', encoding='utf-8') as f:
    t_content = f.read()

# Update Arshi Kabir role
t_content = t_content.replace('<h4>Director</h4>', '<h4>Founder &amp; Director</h4>')

# Update Card 2 to Rumi Kabir
old_card2 = '''                    <div class="col-lg-3 col-md-6">
                        <div class="single-teacher mb-45">
                            <div class="single-teacher-img">
                                <a href="teacher-details.html"><img src="img/teacher/teacher2.jpg" alt="Nizamuddin Ahmad"></a>  
                            </div>
                            <div class="single-teacher-content text-center">
                                <h2><a href="teacher-details.html">Nizamuddin Ahmad</a></h2>
                                <h4>Founder &amp; Secretary</h4>
                                <ul>
                                    <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                                    <li><a href="#"><i class="fa fa-envelope"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>'''

new_card2 = '''                    <div class="col-lg-3 col-md-6">
                        <div class="single-teacher mb-45">
                            <div class="single-teacher-img">
                                <a href="about.html"><img src="img/teacher/rumi-kabir.jpg" alt="Rumi Kabir"></a>  
                            </div>
                            <div class="single-teacher-content text-center">
                                <h2><a href="about.html">Rumi Kabir</a></h2>
                                <h4>Management &amp; Administration</h4>
                                <ul>
                                    <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                                    <li><a href="mailto:idealschool4938@gmail.com"><i class="fa fa-envelope"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>'''
t_content = t_content.replace(old_card2, new_card2)

# Update Homa Parveen card
t_content = t_content.replace(
    '<h4>Senior Teacher (MA, B.Ed)</h4>',
    '<h4>Principal (M.A., B.Ed.)</h4>'
)

# Update faculty roster table:
t_content = t_content.replace(
    '<tr><td>1</td><td>Homa Parveen</td><td>M.A.</td><td>B.Ed.</td><td>Senior Language &amp; Social Science</td></tr>',
    '<tr><td>1</td><td>Homa Parveen</td><td>M.A.</td><td>B.Ed.</td><td>Principal / Senior Language</td></tr>'
)

t_content = t_content.replace(
    '<tr><td>10</td><td>Amarjeet Kumar</td><td>B.A.</td><td>Certified</td><td>Primary Studies</td></tr>',
    '<tr><td>10</td><td>Amarjeet Kumar</td><td>B.A.</td><td>B.Ed.</td><td>Primary Studies &amp; Science</td></tr>'
)

# Add staff group photo feature before the roster table
staff_group_feature = '''                <!-- Faculty Group Spotlight -->
                <div class="row pt-20 pb-50">
                    <div class="col-12 text-center">
                        <div style="background:#f9f6f2; padding:30px; border-radius:6px; border:1px solid #e0d5c8;">
                            <h3 style="color:#34261D; font-weight:700; margin-bottom:10px;">OUR DEDICATED TEACHING FACULTY &amp; STAFF</h3>
                            <p class="mb-25" style="max-width:750px; margin-left:auto; margin-right:auto;">Our certified educators and caring teachers fostering academic foundation, discipline, and moral values for students in Aranda, Hasanpura.</p>
                            <img src="img/teacher/faculty-staff-group.jpg" alt="Ideal Public School Teaching Faculty &amp; Staff" style="width:100%; max-width:960px; border-radius:6px; box-shadow:0 8px 25px rgba(0,0,0,0.12);">
                        </div>
                    </div>
                </div>'''

if '<!-- Faculty Group Spotlight -->' not in t_content:
    t_content = t_content.replace(
        '<div class="row pt-40">\n                    <div class="col-12">\n                        <h3 class="mb-20" style="color:#34261D; font-weight:700;">OFFICIAL FACULTY ROSTER',
        f'{staff_group_feature}\n\n                <div class="row pt-40">\n                    <div class="col-12">\n                        <h3 class="mb-20" style="color:#34261D; font-weight:700;">OFFICIAL FACULTY ROSTER'
    )

with open('teacher.html', 'w', encoding='utf-8') as f:
    f.write(t_content)
print("Updated teacher.html successfully!")


# ----------------------------------------------------
# 3. UPDATE ADMISSIONS.HTML (Fee structure & RTE)
# ----------------------------------------------------
print("--- 3. Updating admissions.html ---")
with open('admissions.html', 'r', encoding='utf-8') as f:
    adm_content = f.read()

old_fee_pattern = re.compile(
    r'<!-- Fee Structure Table -->.*?<!-- RTE Free Quota Section -->.*?</div>\s*</div>',
    re.DOTALL
)

new_fee_section = '''<!-- Fee Structure Table -->
                        <h3 class="mb-20 pt-20" style="color:#34261D; font-weight:700;">REVISED TRANSPARENT FEE STRUCTURE (SESSION 2026-27)</h3>
                        <p class="mb-15">Ideal Public School Aranda maintains an affordable, highly transparent fee policy with no hidden charges or capitation levies. All amounts are in Indian Rupees (₹).</p>
                        <table class="custom-table">
                            <thead>
                                <tr>
                                    <th>Class / Grade Level</th>
                                    <th>Monthly Tuition Fee</th>
                                    <th>One-Time Admission Charge</th>
                                    <th>Curriculum Pattern</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><strong>Nursery (Nur)</strong></td><td>₹ 500 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Foundational Pattern</td></tr>
                                <tr><td><strong>L.K.G</strong></td><td>₹ 600 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Foundational Pattern</td></tr>
                                <tr><td><strong>U.K.G</strong></td><td>₹ 600 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Foundational Pattern</td></tr>
                                <tr><td><strong>Class I</strong></td><td>₹ 700 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Primary Curriculum</td></tr>
                                <tr><td><strong>Class II</strong></td><td>₹ 700 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Primary Curriculum</td></tr>
                                <tr><td><strong>Class III</strong></td><td>₹ 750 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Primary Curriculum</td></tr>
                                <tr><td><strong>Class IV</strong></td><td>₹ 750 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Primary Curriculum</td></tr>
                                <tr><td><strong>Class V</strong></td><td>₹ 800 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Primary Curriculum</td></tr>
                                <tr><td><strong>Class VI</strong></td><td>₹ 800 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Middle School Curriculum</td></tr>
                                <tr><td><strong>Class VII</strong></td><td>₹ 900 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Middle School Curriculum</td></tr>
                                <tr><td><strong>Class VIII</strong></td><td>₹ 900 / month</td><td>₹ 1,000</td><td>CBSE &amp; NCERT Middle School Curriculum</td></tr>
                            </tbody>
                        </table>

                        <div class="row pt-25 mb-25">
                            <div class="col-md-6 mb-20">
                                <div style="background:#f9f6f2; border-left:4px solid #34261D; padding:18px; border-radius:4px; height:100%;">
                                    <h5 style="color:#34261D; margin-bottom:8px; font-weight:700;"><i class="fa fa-book"></i> Prescribed Books Policy</h5>
                                    <p style="font-size:14px; margin:0; line-height:1.6;">Textbooks are strictly aligned with <strong>NCERT + CBSE</strong> guidelines. Parents can purchase books from any standard bookstore/shop in the open market (<em>No mandatory in-house bookshop purchases</em>).</p>
                                </div>
                            </div>
                            <div class="col-md-6 mb-20">
                                <div style="background:#fdf2f2; border-left:4px solid #c0392b; padding:18px; border-radius:4px; height:100%;">
                                    <h5 style="color:#c0392b; margin-bottom:8px; font-weight:700;"><i class="fa fa-ban"></i> Re-Admission Policy</h5>
                                    <p style="font-size:14px; margin:0; line-height:1.6;"><strong>Re-admission is strictly not allowed.</strong> Once enrolled, students progress naturally each year without repetitive re-admission costs or duplicate registration fees.</p>
                                </div>
                            </div>
                        </div>

                        <!-- RTE Free Quota Section -->
                        <div id="rte" class="rte-box p-4 mt-20" style="background:#f5f0eb; border: 2px dashed #34261D; border-radius: 6px;">
                            <h3 style="color:#34261D; font-weight:700;"><i class="fa fa-certificate"></i> RTE ACT 2009 — 25% FREE ADMISSIONS &amp; ZERO CHARGES</h3>
                            <p>Under Section 12(1)(c) of the Right of Children to Free and Compulsory Education (RTE) Act 2009 and Govt. Registration <strong>RTE/SWN/2014-15 0079</strong>, <strong>RTE admitted students receive 100% Free Admission and All School Charges Free</strong> (tuition fees, examination fees, and developmental charges are entirely waived).</p>
                            <p><strong>Required for RTE Admission:</strong> Income certificate / BPL ration card, caste certificate (if applicable), proof of residence within Hasanpura/Aranda, child's birth certificate, and Aadhaar card.</p>
                        </div>
                    </div>'''

if old_fee_pattern.search(adm_content):
    adm_content = old_fee_pattern.sub(new_fee_section, adm_content)
    print("Updated fee schedule and admission policies in admissions.html")
else:
    print("WARNING: Could not find fee pattern in admissions.html")

with open('admissions.html', 'w', encoding='utf-8') as f:
    f.write(adm_content)


# ----------------------------------------------------
# 4. UPDATE COURSE-DETAILS.HTML & COURSE.HTML (Pre-primary & CBSE/NCERT)
# ----------------------------------------------------
print("--- 4. Updating course-details.html ---")
with open('course-details.html', 'r', encoding='utf-8') as f:
    cd_content = f.read()

preprimary_section = '''                                    <div class="single-course-left" style="background:#fdfaf7; border-left:4px solid #34261D; padding:20px; border-radius:4px; margin-bottom:30px;">
                                        <h3 style="color:#34261D; font-weight:700; margin-bottom:12px;"><i class="fa fa-child"></i> Pre-Primary Wing Course Details (Nursery, LKG, UKG)</h3>
                                        <p>Our foundational pre-primary program is structured around experiential, joyful, and play-based learning adhering to the National Curriculum Framework (NCF) and <strong>CBSE &amp; NCERT pattern</strong>:</p>
                                        <ul style="list-style-type:disc; padding-left:25px; line-height:1.8;">
                                            <li><strong>Nursery:</strong> Social socialization, phonics through nursery rhymes, color &amp; shape identification, motor skill enhancement with modeling clay, and basic conversational vocabulary.</li>
                                            <li><strong>Lower Kindergarten (LKG):</strong> English alphabet writing &amp; sounds, Hindi वर्णमाला (Akshar) identification, number concepts (1 to 50), simple patterns, and environmental awareness.</li>
                                            <li><strong>Upper Kindergarten (UKG):</strong> Word-building (two- and three-letter words), basic sentence formation, Hindi स्वर व व्यंजन लेखन, addition and subtraction readiness (numbers 1 to 100), good habits, and general etiquette.</li>
                                        </ul>
                                    </div>'''

if '<!-- Pre-Primary Wing Course Details -->' not in cd_content:
    cd_content = cd_content.replace(
        '<div class="single-course-left">\n                                        <h3>Subjects Offered</h3>',
        f'{preprimary_section}\n\n                                    <div class="single-course-left">\n                                        <h3>Subjects Offered</h3>'
    )
    with open('course-details.html', 'w', encoding='utf-8') as f:
        f.write(cd_content)
    print("Added Pre-Primary course details into course-details.html")


# ----------------------------------------------------
# 5. CREATE SPORTS.HTML (Dedicated Sports & Games Page)
# ----------------------------------------------------
print("--- 5. Creating dedicated sports.html ---")
sports_html_content = '''<!doctype html>
<html class="no-js" lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <title>Sports & Physical Education | Ideal Public School Aranda</title>
        <meta name="description" content="Sports programs, games facilities, athletic training, and physical fitness at Ideal Public School Aranda, Hasanpura, Siwan.">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <link rel="stylesheet" href="css/animate.min.css">
        <link rel="stylesheet" href="css/meanmenu.css">
        <link rel="stylesheet" href="css/magnific-popup.css">
        <link rel="stylesheet" href="css/owl.carousel.min.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">
        <link rel="stylesheet" href="css/et-line-icon.css">
        <link rel="stylesheet" href="css/reset.css">
        <link rel="stylesheet" href="css/ionicons.min.css">
        <link rel="stylesheet" href="css/material-design-iconic-font.min.css">
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="css/responsive.css">
        <script src="js/vendor/modernizr-3.11.2.min.js"></script>
    </head>
    <body>
        <!-- Header Area Start -->
		<header class="top">
		    <div class="header-top">
		        <div class="container">
		            <div class="row">
		                <div class="col-md-8 col-sm-8">
		                    <div class="header-top-left">
		                        <p><i class="fa fa-phone"></i> +91 9934991694 / 9262683463 &nbsp;|&nbsp; <i class="fa fa-map-marker"></i> Aranda, Hasanpura, Siwan &nbsp;|&nbsp; <span class="badge-rte">RTE/SWN/2014-15 0079</span></p>
		                    </div>
		                </div>
		                <div class="col-md-4 col-sm-4">
		                    <div class="header-top-right text-md-end text-center">
		                        <ul>
		                            <li><a href="admissions.html">Admissions 2026-27</a></li>
		                            <li><a href="books.html">Prescribed Books</a></li>
		                        </ul>
		                    </div>
		                </div>
		            </div>
		        </div>
		    </div>
			<div class="header-area two header-sticky">
				<div class="container">
					<div class="row">
						<div class="col-md-3 col-sm-5 col-6">
							<div class="logo">
								<a href="index.html"><img src="img/logo/logo2.png" alt="Ideal Public School Aranda" /></a>
							</div>
						</div>
						<div class="col-md-9 col-sm-7 col-6">
                            <div class="content-wrapper text-end">
                                <!-- Main Menu Start -->
                                <div class="main-menu">
                                    <nav>
                                        <ul>
                                            <li><a href="index.html">Home</a></li>
                                            <li><a href="about.html">About</a></li>
                                            <li><a href="course.html">Academics</a>
                                                <ul>
                                                    <li><a href="course.html">Academic Wings (Nur - VIII)</a></li>
                                                    <li><a href="course-details.html">CBSE Curriculum Details</a></li>
                                                    <li><a href="books.html">Prescribed Books &amp; Prices</a></li>
                                                </ul>
                                            </li>
                                            <li><a href="admissions.html">Admissions</a>
                                                <ul>
                                                    <li><a href="admissions.html">Admission Process &amp; Fees</a></li>
                                                    <li><a href="admissions.html#rte">RTE 25% Free Quota</a></li>
                                                </ul>
                                            </li>
                                            <li><a href="facilities.html">Campus</a>
                                                <ul>
                                                    <li><a href="facilities.html">Campus Facilities &amp; Labs</a></li>
                                                    <li><a href="student-life.html">Student Life &amp; Houses</a></li>
                                                    <li><a href="sports.html">Sports &amp; Games</a></li>
                                                    <li><a href="gallery.html">Photo Gallery</a></li>
                                                </ul>
                                            </li>
                                            <li><a href="sports.html" class="active">Sports</a></li>
                                            <li><a href="teacher.html">Faculty</a>
                                                <ul>
                                                    <li><a href="teacher.html">Faculty Roster</a></li>
                                                    <li><a href="teacher-details.html">Leadership Profile</a></li>
                                                </ul>
                                            </li>
                                            <li><a href="event.html">Events &amp; Notices</a>
                                                <ul>
                                                    <li><a href="event.html">Upcoming Events</a></li>
                                                    <li><a href="blog.html">School Notices &amp; News</a></li>
                                                </ul>
                                            </li>
                                            <li><a href="contact.html">Contact</a></li>
                                        </ul>
                                    </nav>
                                </div>
                                <!-- Main Menu End -->
                            </div>
						</div>
                        <div class="col-12">
                            <div class="mobile-menu"></div> 
                        </div>
					</div>
				</div>
			</div>
		</header>
		<!-- Header Area End -->

		<!-- Banner Area Start -->
		<div class="banner-area-wrapper">
            <div class="banner-area text-center" style="background-image: url('img/banner/banner.jpg');">	
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <div class="banner-content-wrapper">
                                <div class="banner-content">
                                    <h2>SPORTS, GAMES &amp; PHYSICAL FITNESS</h2> 
                                    <div class="banner-breadcrumb">
                                        <ul>
                                            <li><a href="index.html">home</a> <span class="delimiter">/</span></li>
                                            <li>sports</li>
                                        </ul>
                                    </div>
                                </div> 
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>    
		<!-- Banner Area End -->

        <!-- Sports Overview Area -->
        <div class="courses-details-area pt-150 pb-120">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="courses-details">
                            <div class="courses-details-img mb-30">
                                <img src="img/sports/sports-assembly.jpg" alt="Students in Sports &amp; Republic Day Formation" style="width:100%; border-radius:4px; box-shadow:0 8px 25px rgba(0,0,0,0.1);">
                            </div>
                            <div class="course-details-content">
                                <h2>HOLISTIC ATHLETICS &amp; PHYSICAL EDUCATION</h2>
                                <p>At <strong>Ideal Public School Aranda</strong>, physical education is an integral pillar of our educational ethos. We believe that true learning encompasses mental sharpness, physical agility, teamwork, and sportsman spirit. Under the guidance of trained physical instructors, every student participates in scheduled daily outdoor and indoor sports.</p>
                                
                                <h3 class="mt-40 mb-20" style="color:#34261D; font-weight:700;"><i class="fa fa-trophy"></i> Sports &amp; Games Disciplines</h3>
                                <div class="row">
                                    <div class="col-md-6 mb-25">
                                        <div style="background:#f9f6f2; border:1px solid #e2d9cd; padding:20px; border-radius:4px; height:100%;">
                                            <h4 style="color:#34261D; font-weight:700; margin-bottom:10px;"><i class="fa fa-futbol-o"></i> Outdoor Sports</h4>
                                            <ul style="list-style-type:disc; padding-left:20px; line-height:1.8;">
                                                <li><strong>Cricket:</strong> Pitch play, batting, bowling, and inter-house matches</li>
                                                <li><strong>Football:</strong> Field training, passing drills, and mini-leagues</li>
                                                <li><strong>Volleyball:</strong> Standard court play &amp; agility drills</li>
                                                <li><strong>Kabaddi &amp; Kho-Kho:</strong> Traditional Indian endurance and agility sports</li>
                                                <li><strong>Track &amp; Field Athletics:</strong> 100m/200m sprints, relay races, and long jump</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="col-md-6 mb-25">
                                        <div style="background:#f9f6f2; border:1px solid #e2d9cd; padding:20px; border-radius:4px; height:100%;">
                                            <h4 style="color:#34261D; font-weight:700; margin-bottom:10px;"><i class="fa fa-gamepad"></i> Indoor &amp; Mind Games</h4>
                                            <ul style="list-style-type:disc; padding-left:20px; line-height:1.8;">
                                                <li><strong>Badminton:</strong> Singles and doubles tournament coaching</li>
                                                <li><strong>Table Tennis:</strong> Reflex and coordination training</li>
                                                <li><strong>Chess:</strong> Strategic thinking and cognitive tournaments</li>
                                                <li><strong>Carrom:</strong> Recreational and focused indoor play</li>
                                                <li><strong>Yoga &amp; Pranayama:</strong> Daily morning breathing exercises and flexibility asanas</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>

                                <h3 class="mt-20 mb-20" style="color:#34261D; font-weight:700;"><i class="fa fa-flag"></i> Annual Sports Meet &amp; March Past</h3>
                                <p>Every academic session culminates in the <strong>Annual Inter-House Sports Championship</strong> where the Blue, Green, Red, and Gold houses compete across sprints, relays, tug-of-war, and team sports. Our disciplined student parade and flag march during national festivals showcase precision marching, leadership, and national pride.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="blog-sidebar right">
                            <div class="single-blog-widget mb-50">
                                <h3>SPORTS HIGHLIGHTS</h3>
                                <ul>
                                    <li><a href="#">Dedicated School Playground</a></li>
                                    <li><a href="#">Full-Time Certified P.E. Teachers</a></li>
                                    <li><a href="#">Daily Morning Yoga &amp; PT Assembly</a></li>
                                    <li><a href="#">Annual Inter-House Tournaments</a></li>
                                    <li><a href="#">District Level Sports Participation</a></li>
                                    <li><a href="#">First-Aid &amp; Sports Safety Facility</a></li>
                                </ul>
                            </div>
                            <div class="single-blog-widget mb-50">
                                <h3>SPORTS PHOTO SPOTLIGHT</h3>
                                <div class="single-post">
                                    <div class="single-post-img">
                                        <a href="gallery.html"><img src="img/sports/sports1.jpg" alt="Republic Day Assembly" style="width:100%; border-radius:4px;"></a>
                                    </div>
                                    <div class="single-post-content mt-15">
                                        <h4><a href="gallery.html">Patriotic March &amp; Athletic Formations</a></h4>
                                        <p>Students assembled in athletic formation during Republic Day celebration at Ideal Public School ground.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer Area Start -->
        <footer class="footer-area">
            <div class="main-footer">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-4 col-md-6">
                            <div class="single-widget pr-60">
                                <div class="footer-logo pb-25">
                                    <a href="index.html"><img src="img/logo/footer-logo.png" alt="Ideal Public School Aranda"></a>
                                </div>
                                <p>Ideal Public School Aranda is dedicated to quality education from Nursery to Class VIII in Hasanpura, Siwan under the CBSE and NCERT pattern.</p>
                                <div class="footer-social">
                                    <ul>
                                        <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                                        <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                                        <li><a href="#"><i class="fa fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6">
                            <div class="single-widget">
                                <h3>Quick Links</h3>
                                <ul>
                                    <li><a href="about.html">About Our School</a></li>
                                    <li><a href="course.html">Academics &amp; Curriculum</a></li>
                                    <li><a href="admissions.html">Admissions 2026-27</a></li>
                                    <li><a href="sports.html">Sports &amp; Games</a></li>
                                    <li><a href="facilities.html">Campus Facilities</a></li>
                                    <li><a href="teacher.html">Faculty Roster</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-6">
                            <div class="single-widget">
                                <h3>Useful Info</h3>
                                <ul>
                                    <li><a href="books.html">Prescribed Books</a></li>
                                    <li><a href="admissions.html#rte">RTE 25% Free Quota</a></li>
                                    <li><a href="gallery.html">Photo Gallery</a></li>
                                    <li><a href="event.html">Upcoming Events</a></li>
                                    <li><a href="contact.html">Contact Us</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6">
                            <div class="single-widget">
                                <h3>Get In Touch</h3>
                                <p>Aranda, Hasanpura, Siwan, Bihar - 841236</p>
                                <p>Phone: +91 9934991694 / 9262683463</p>
                                <p>Email: idealschool4938@gmail.com</p>
                                <p>Govt Reg: RTE/SWN/2014-15 0079</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom text-center">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <p>© 2026 Ideal Public School Aranda. All Rights Reserved. CBSE &amp; NCERT Pattern.</p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- Footer Area End -->

        <script src="js/vendor/jquery-3.6.0.min.js"></script>
        <script src="js/bootstrap.bundle.min.js"></script>
        <script src="js/jquery.meanmenu.js"></script>
        <script src="js/jquery.magnific-popup.js"></script>
        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
    </body>
</html>'''

with open('sports.html', 'w', encoding='utf-8') as f:
    f.write(sports_html_content)
print("Created sports.html successfully!")


# ----------------------------------------------------
# 6. UPDATE GALLERY.HTML (Add Campus 4 Categories)
# ----------------------------------------------------
print("--- 6. Updating gallery.html ---")
with open('gallery.html', 'r', encoding='utf-8') as f:
    gal_content = f.read()

# Add Campus Categories section at the top of gallery grid
campus_categories_html = '''                <!-- Campus Categories (Classrooms, Library, Playground, Labs) -->
                <div class="row mb-50">
                    <div class="col-12">
                        <div style="background:#f9f6f2; border:1px solid #e2d9cd; padding:25px; border-radius:6px;">
                            <h3 style="color:#34261D; font-weight:700; margin-bottom:15px; text-align:center;"><i class="fa fa-university"></i> CAMPUS FACILITIES AT A GLANCE</h3>
                            <div class="row text-center">
                                <div class="col-md-3 col-6 mb-15">
                                    <div style="background:#fff; padding:15px; border-radius:4px; border:1px solid #eee;">
                                        <i class="fa fa-graduation-cap" style="font-size:28px; color:#34261D; margin-bottom:10px;"></i>
                                        <h5 style="color:#34261D; margin:0; font-weight:700;">1. Classrooms</h5>
                                        <p style="font-size:13px; color:#666; margin:5px 0 0;">27 Spacious, ventilated smart rooms</p>
                                    </div>
                                </div>
                                <div class="col-md-3 col-6 mb-15">
                                    <div style="background:#fff; padding:15px; border-radius:4px; border:1px solid #eee;">
                                        <i class="fa fa-book" style="font-size:28px; color:#34261D; margin-bottom:10px;"></i>
                                        <h5 style="color:#34261D; margin:0; font-weight:700;">2. School Library</h5>
                                        <p style="font-size:13px; color:#666; margin:5px 0 0;">Reference books, journals &amp; literature</p>
                                    </div>
                                </div>
                                <div class="col-md-3 col-6 mb-15">
                                    <div style="background:#fff; padding:15px; border-radius:4px; border:1px solid #eee;">
                                        <i class="fa fa-futbol-o" style="font-size:28px; color:#34261D; margin-bottom:10px;"></i>
                                        <h5 style="color:#34261D; margin:0; font-weight:700;">3. Playground</h5>
                                        <p style="font-size:13px; color:#666; margin:5px 0 0;">Outdoor athletics &amp; sports field</p>
                                    </div>
                                </div>
                                <div class="col-md-3 col-6 mb-15">
                                    <div style="background:#fff; padding:15px; border-radius:4px; border:1px solid #eee;">
                                        <i class="fa fa-flask" style="font-size:28px; color:#34261D; margin-bottom:10px;"></i>
                                        <h5 style="color:#34261D; margin:0; font-weight:700;">4. School Labs</h5>
                                        <p style="font-size:13px; color:#666; margin:5px 0 0;">Computer science &amp; science lab</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

if '<!-- Campus Categories' not in gal_content:
    gal_content = gal_content.replace(
        '<div class="row">\n                    <!-- Gallery Item 1 -->',
        f'{campus_categories_html}\n\n                <div class="row">\n                    <!-- Gallery Item 1 -->'
    )

    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(gal_content)
    print("Added Campus categories into gallery.html")


# ----------------------------------------------------
# 7. UPDATE CONTACT.HTML (Registration No & Email)
# ----------------------------------------------------
print("--- 7. Updating contact.html ---")
with open('contact.html', 'r', encoding='utf-8') as f:
    c_content = f.read()

c_content = c_content.replace(
    '<p>idealpublichighschool2005@gmail.com<br>Recognized under RTE Act 2009 (RTE/SWN/2014-15 0079)</p>',
    '<p><strong>idealschool4938@gmail.com</strong><br>idealpublichighschool2005@gmail.com<br><span class="badge" style="background:#34261D; color:#fff; padding:5px 10px; font-weight:600; border-radius:3px; margin-top:5px; display:inline-block;">Govt. Reg. No: RTE/SWN/2014-15 0079</span></p>'
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(c_content)
print("Updated contact.html successfully!")


# ----------------------------------------------------
# 8. UPDATE NAVIGATION IN ALL 16 PAGES (Include Sports page & update email)
# ----------------------------------------------------
print("--- 8. Updating navigation in all pages ---")
for p in all_pages:
    with open(p, 'r', encoding='utf-8') as f:
        page_html = f.read()

    # Add Sports link in Campus dropdown if not already present
    if '<li><a href="sports.html">Sports &amp; Games</a></li>' not in page_html:
        page_html = page_html.replace(
            '<li><a href="student-life.html">Student Life &amp; Houses</a></li>\n                                                    <li><a href="gallery.html">Photo Gallery</a></li>',
            '<li><a href="student-life.html">Student Life &amp; Houses</a></li>\n                                                    <li><a href="sports.html">Sports &amp; Games</a></li>\n                                                    <li><a href="gallery.html">Photo Gallery</a></li>'
        )
    
    # Update email in footer and header where applicable
    page_html = page_html.replace(
        'Email: idealpublichighschool2005@gmail.com',
        'Email: idealschool4938@gmail.com'
    )
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(page_html)

print("Navigation and metadata updated across all pages!")
