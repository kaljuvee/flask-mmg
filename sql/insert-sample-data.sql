-- Users Table
INSERT INTO Users (email, password_hash, first_name, last_name, phone_number)
VALUES
('clinic1@example.com', 'hashedpassword1', 'John', 'Doe', '1234567890'),
('patient1@example.com', 'hashedpassword2', 'Jane', 'Smith', '0987654321'),
('admin@example.com', 'hashedpassword3', 'Alice', 'Johnson', '1122334455');

-- Roles Table
INSERT INTO Roles (role_name)
VALUES
('Service Provider'),
('Customer'),
('Administrator'),
('Partner');

-- UserRoles Table (Join Table for Users and Roles)
INSERT INTO UserRoles (user_id, role_id)
VALUES
(1, 1), -- Clinic user
(2, 2), -- Patient user
(3, 3); -- Administrator user

-- Clinics Table
INSERT INTO Clinics (user_id, clinic_name, address, contact_details, specialty_areas)
VALUES
(1, 'Health Clinic One', '123 Health St, Wellness City', 'healthclinic1@example.com, +123456789', 'Cardiology, Orthopedics');

-- Services Table
INSERT INTO Services (service_name, description, pricing, expected_duration)
VALUES
('Cardiac Consultation', 'Detailed cardiac consultation and diagnosis', 200.00, '00:30:00'),
('Orthopedic Surgery', 'Surgical treatment for orthopedic conditions', 5000.00, '03:00:00');

-- ServiceListings Table (Join Table for Clinics and Services)
INSERT INTO ServiceListings (clinic_id, service_id, customization_options, special_packages)
VALUES
(1, 1, 'N/A', 'Discount for multiple consultations'),
(1, 2, 'N/A', 'Pre-surgery and post-surgery package');

-- Reviews Table
INSERT INTO Reviews (clinic_id, user_id, rating, comment)
VALUES
(1, 2, 5, 'Excellent service and very professional staff.'),
(1, 2, 4, 'Good experience but waiting time was a bit long.');

-- Appointments Table
INSERT INTO Appointments (patient_id, service_listing_id, appointment_time, status)
VALUES
(2, 1, '2024-08-05 09:00:00', 'Scheduled'),
(2, 2, '2024-08-10 14:00:00', 'Scheduled');

-- Documents Table
INSERT INTO Documents (user_id, document_type, document_path)
VALUES
(1, 'License', '/path/to/license.pdf'),
(2, 'Passport', '/path/to/passport.pdf');

-- Payments Table
INSERT INTO Payments (appointment_id, amount, payment_method, payment_status)
VALUES
(1, 200.00, 'Stripe', 'Paid'),
(2, 5000.00, 'Paypal', 'Pending');

-- Notifications Table
INSERT INTO Notifications (user_id, message)
VALUES
(2, 'Your appointment with Health Clinic One has been scheduled for 2024-08-05 at 09:00.'),
(2, 'Your appointment with Health Clinic One has been scheduled for 2024-08-10 at 14:00.');

-- Partners Table
INSERT INTO Partners (partner_name, services_offered, contact_info)
VALUES
('TravelAssist', 'Travel planning and booking services', 'contact@travelassist.com, +1987654321');

-- CRM Integrations Table
INSERT INTO CRMIntegrations (crm_name, api_key, settings)
VALUES
('PipeDrive', 'api_key_pipedrive', '{"integration": "enabled", "sync_interval": "daily"}'),
('FreshDesk', 'api_key_freshdesk', '{"integration": "enabled", "support_email": "support@freshdesk.com"}');
